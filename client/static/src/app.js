var clientApp = angular.module('clientApp', ['ngRoute']);

clientApp.config(function($routeProvider) {
        $routeProvider.
          when('/', {
            templateUrl: 'static/power-list.html',
            controller: 'NodeListController'
          }).
          when('/power/:nodeID', {
            templateUrl: 'static/power-list.html',
            controller: 'PowerDetailController'
          }).
          otherwise({
            redirectTo: '/'
          });
      });

clientApp.controller('NodeListController',
    ['$scope', '$http', '$timeout', '$route', function(scope, http, timeout, route){
        http.get(Server.ADDRESS + 'data/api/node'
                 + '/?format=json').success(function(d){
            scope.nodeList = d;
            refreshMarkers(d);
        });

        var pollList = function() {
            polling = true;
            timeout(function() {
                http.get(Server.ADDRESS + 'data/api/update'
                    + '/?format=json').then(function successCallback(response){
                    if((response.data[0].update_check*1000) > (new Date).getTime()-5000){
                        http.get(Server.ADDRESS + 'data/api/node'
                                 + '/?format=json').success(function(d){
                            scope.nodeList = d;
                            refreshMarkers(d);
                            route.reload();
                        })
                    }else{

                    }
                }, function errorCallback(response){
                    console.log("Error retrieving update");
                })
                pollList();
            }, 2000);
        };

        if(!polling){
            pollList();
        }

        var refreshMarkers = function(d) {

          for (var i = 0; i < d.length; i++) {
            var marker = d[i];

            // make sure this marker hasn't been added to the map already
            if (!(marker.id in markers)) {

              // DEBUG:  For now it just grabs a default component icon information
              var component = defaultComponentsArr[nodeType(d.type)];
              var latlng = L.latLng(marker.latitude, marker.longitude);

              var newIcon = new compIcon({
                  iconUrl: component.Icon,
                  iconAnchor: [defaultIconSize.x/2.0, defaultIconSize.y/2.0]
                });
              var options = {
        						icon: newIcon,
        						clickable: true,
        						draggable: true,
                    keyboard: false
                  };

              addMarkerToMap(marker.id, component, latlng, options);
            }
          }
        }

        scope.nodeListClicked = function(nodeID, type){
            var data;
            http.get(Server.ADDRESS + 'data/api/' + nodeType(type) + '/'
                + nodeID + '/?format=json').success(function(d){
                loadComponent(d);
            })
        }
    }
]);

clientApp.controller('PowerDetailController',
    ['$scope', '$http', '$routeParams', function(scope, http, params){
        http.get(Server.ADDRESS + 'data/api/power/'
            + params.nodeID + '/?format=json').success(function(data){
            scope.power = data;
        })
    }
]);

function loadComponent(data){
    selectedComponent = data;
    var componentTable = document.getElementById('componentTable');
    for(var i = componentTable.rows.length-1; i > 1; i--){
        componentTable.deleteRow(i);
    }
    var tr, td;
    var keys = Object.keys(data);
    for(var i = 0; i < keys.length; i++){
        tr = document.createElement('tr');
        td = document.createElement('td');
        td.className = "rowName";
        if(keys[i] != 'id' && keys[i] != 'type'){
            td.innerHTML = formatTableName(keys[i]);
            tr.appendChild(td);
        }
        if(i+1 == keys.length){
            td.style = "padding-bottom: 15px";
        }
        td = document.createElement('td');
        td.id = keys[i];
        td.className = "rowData";
        if(keys[i] != 'id' && keys[i] != 'type'){
            if(keys[i] == 'operational_status'){
                createToggle(td, "1", data[keys[i]]);
                tr.appendChild(td);
            }else if(keys[i] == 'is_bus'){
                createToggle(td, "2", data[keys[i]]);
                tr.appendChild(td);
            }else if(keys[i] == 'stiffness'){
                createToggle(td, "3", data[keys[i]]);
                tr.appendChild(td);
            }else if(keys[i] == 'created_date'){
                var date = new Date(data[keys[i]]*1000);
                var day = date.getDate();
                var monthIndex = date.getMonth();
                var year = date.getFullYear();
                td.innerHTML = monthNames[monthIndex] + ' ' + day + ', ' + year;
            }else{
                td.onclick = function(e){editComponent(this)};
                td.innerHTML = data[keys[i]];
            }
        }
        tr.appendChild(td);
        componentTable.tBodies[0].appendChild(tr);
    }
    td.style = "padding-bottom: 15px";
}

function createToggle(td, count, value){
    var input = document.createElement('input');
    var label = document.createElement('label');
    input.className = "cmn-toggle cmn-toggle-round";
    input.setAttribute("type", "checkbox");
    input.id = "cmn-toggle-"+count;
    label.setAttribute('for', "cmn-toggle-"+count);
    input.checked = value;
    input.onclick = function(e){toggleClicked(td.id)};
    td.appendChild(input);
    td.appendChild(label);
}
