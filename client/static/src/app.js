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
        // Initialize global info
        initPowerNetwork();

        // Initial node list GET
        http.get(Server.ADDRESS + 'data/api/node'
                 + '/?format=json').success(function(d){
            scope.nodeList = d;
            refreshMarkers(d);
        });
        http.get(Server.ADDRESS + 'data/api/connection'
                 + '/?format=json').success(function(d){
            refreshConnections(d);
        });

        // Server poll for updates
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
                          });
                        http.get(Server.ADDRESS + 'data/api/connection'
                                 + '/?format=json').success(function(d){
                            refreshConnections(d);
                            route.reload();
                        });
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

        var refreshConnections = function(d) {
          for (var i = 0; i < d.length; i++) {
            var connection = d[i];
            var from_marker = markers[connection.from_bus_id];
            var to_marker = markers[connection.to_bus_id];
            if (from_marker != undefined && to_marker != undefined) {
              if(!(connection.id in connections))
                addConnectionToMap(connection.id, connection.type, from_marker, to_marker, polylineOptions)
            } else {
              console.log("WARNING: Received A Connection, but couldn't find related markers!!");
            }
            //var polyLine = new L.Polyline([from_marker._latlng, to_marker._latlng], polylineOptions);
            //polyLine.addTo(map);
            //polyLine.on('click', handleConnectionClick);
            //console.log("Received connection:" + connection);
          }
        }

        var refreshMarkers = function(d) {

          for (var i = 0; i < d.length; i++) {
            var marker = d[i];

            // make sure this marker hasn't been added to the map already
            if (!(marker.id in markers)) {

              var component = defaultComponentsArr[nodeType(marker.type)];
              var latlng = L.latLng(marker.latitude, marker.longitude);

              var newIcon = new nodeIcon({
                  iconUrl: component.Icon
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

        // Load component table
        scope.nodeListClicked = function(nodeID, type){
            var data;
            http.get(Server.ADDRESS + 'data/api/' + nodeType(type) + '/'
                + nodeID + '/?format=json').success(function(d){
                loadComponent(d, true);
            })
        }

        scope.isLoad = function(type) {
          if (type == '0'){
            console.log("LOAD");
            return true;
          }
          else{
            return false;
          }
        }

        scope.isSyncGen = function(type) {
          if (type == '1'){
            console.log("Sync");
            return true;
          }
          else{
            return false;
          }
        }

        scope.isBus = function(type) {
          if (type == '2'){
            console.log("Bus");
            return true;
          }
          else{
            return false;
          }
        }

        scope.isUtility = function(type) {
          if (type == '3'){
            console.log("Utility");
            return true;
          }
          else{
            return false;
          }
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

function loadComponent(data, isNode){
    selectedComponent = data;
    var componentTable = document.getElementById('componentTable');
    for(var i = componentTable.rows.length-1; i > 1; i--){
        componentTable.deleteRow(i);
    }
    var tr, td;
    var keys = Object.keys(data);

    var coordIndices = new Array(2);
    coordIndices[0] = new Array(4);
    coordIndices[1] = new Array(4);
    var hasCoordIndices = false;

    for(var i = 0; i < keys.length; i++){
        tr = document.createElement('tr');
        td = document.createElement('td');
        td.className = "rowName";
        if(keys[i] == 'type'){
            var compTitle = document.getElementById('compTitle');
            if(isNode){
                compTitle.innerHTML = nodeTypeDisplay(data[keys[i]]);
            }else{
                compTitle.innerHTML = connectionTypeDisplay(data[keys[i]]);
            }
        }
        if(keys[i] != 'id' && keys[i] != 'type'){
            td.innerHTML = formatTableName(keys[i]);
            tr.appendChild(td);
        }
        if(i+1 == keys.length){
            td.style = "padding-bottom: 15px";
        }

        if (keys[i].indexOf("_coordinate") > -1) {
          td = undefined;
        } else {
          td = document.createElement('td');
          td.id = keys[i];
          td.className = "rowData";
        }
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
            }else if(keys[i] == 'x_1_coordinate') {
                coordIndices[0][0] = i;
                hasCoordIndices = true;
            }else if(keys[i] == 'x_2_coordinate') {
                coordIndices[0][1] = i;
                hasCoordIndices = true;
            }else if(keys[i] == 'x_3_coordinate') {
                coordIndices[0][2] = i;
                hasCoordIndices = true;
            }else if(keys[i] == 'x_4_coordinate') {
                coordIndices[0][3] = i;
                hasCoordIndices = true;
            }else if(keys[i] == 'h_1_coordinate') {
                coordIndices[1][0] = i;
                hasCoordIndices = true;
            }else if(keys[i] == 'h_2_coordinate') {
                coordIndices[1][1] = i;
                hasCoordIndices = true;
            }else if(keys[i] == 'h_3_coordinate') {
                coordIndices[1][2] = i;
                hasCoordIndices = true;
            }else if(keys[i] == 'h_4_coordinate') {
                coordIndices[1][3] = i;
                hasCoordIndices = true;
            }else{
                if(isNode){
                    td.onclick = function(e){editNodeComponent(this)};
                }else{
                    td.onclick = function(e){editConnectionComponent(this)};
                }
                td.innerHTML = data[keys[i]];
            }
        }
        if (td != undefined) {
          tr.appendChild(td);
          componentTable.tBodies[0].appendChild(tr);
        }
    }

    if (hasCoordIndices) {
      // Add Header
      tr = document.createElement('tr');
      var th = document.createElement('th');
      th.innerHTML = 'Coordinates:';
      th.className = "colName";
      tr.appendChild(th);
      componentTable.tBodies[0].appendChild(tr);

      tr = document.createElement('tr');
      var thX = document.createElement('th');
      var thH = document.createElement('th');
      thX.innerHTML = 'X';
      thH.innerHTML = 'H';
      thX.className = "colName";
      thH.className = "colName";
      tr.appendChild(thX);
      tr.appendChild(thH);
      componentTable.tBodies[0].appendChild(tr);

      // Add Coordinate Data
      for (var row = 0; row < 4; row++) {
        tr = document.createElement('tr');
        for (var col = 0; col < 2; col++) {
          td = document.createElement('td');
          var index = coordIndices[col][row];
          td.id = keys[index];
          td.className = "rowData";
          td.onclick = function(e){editConnectionComponent(this)};
          td.innerHTML = data[keys[index]];
          tr.appendChild(td);
        }
        componentTable.tBodies[0].appendChild(tr);
      }
    }

    td.style = "padding-bottom: 15px";
}

function formatTableName(name){
    var split = name.split('_');
    var ret = '';
    for(var i = 0; i < split.length; i++){
        ret+= split[i].charAt(0).toUpperCase() + split[i].slice(1) + ' ';
    }
    return ret.slice(0, -1);
}

var editNodeComponent = function(cell){
    var row = cell.parentNode;
    var input = document.createElement("td");
    input.id = cell.id;
    input.innerHTML = "<input class='componentInput' value='" + cell.innerHTML
        + "' onkeydown='postChangeNode(this)'></input>";
    //row.removeChild(cell);
    //row.appendChild(input);
    row.replaceChild(input, cell);
}

var editConnectionComponent = function(cell){
    var row = cell.parentNode;
    var input = document.createElement("td");
    input.id = cell.id;
    input.innerHTML = "<input class='componentInput' value='" + cell.innerHTML
        + "' onkeydown='postChangeConnection(this)'></input>";
    //row.removeChild(cell);
    //row.appendChild(input);
    row.replaceChild(input, cell);
}

var postChangeNode = function(input){
    if(event.keyCode == 13){
        resetCell(input);
        $.ajax({
            url: Server.ADDRESS + "data/api/" + nodeType(selectedComponent.type) + '/'
                + selectedComponent.id + "/" ,
            type: 'PUT',
            data: selectedComponent,
            success: function(result) {
                // Do something with the result
            }
        });
    }
}

var postChangeConnection = function(input){
    if(event.keyCode == 13){
        resetCell(input);
        $.ajax({
            url: Server.ADDRESS + "data/api/" + connectionType(selectedComponent.type) + '/'
                + selectedComponent.id + "/" ,
            type: 'PUT',
            data: selectedComponent,
            success: function(result) {
                // Do something with the result
            }
        });
    }
}

function resetCell(input){
    var cell = input.parentNode;
    var row = cell.parentNode;
    //row.removeChild(cell);
    cell.innerHTML = input.value;
    selectedComponent[cell.id] = input.value;
    cell.className = "rowData";
    cell.onclick = function(e){editComponent(this)};
    cell.id = input.id;
    //row.appendChild(cell);
    //row.replaceChild(cell, input.parentNode);
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

function initPowerNetwork(){
	document.getElementById("ambTempC").innerHTML=0;
	document.getElementById("ambTempF").innerHTML=32;
	document.getElementById("voltUnits").innerHTML='kV';
	document.getElementById("curUnits").innerHTML='A';
	document.getElementById("powUnits").innerHTML='kW';
	document.getElementById("baseFreq").innerHTML='20 kHz';
	document.getElementById("busCount").innerHTML=0;
	document.getElementById("utilCount").innerHTML=0;
	document.getElementById("genCount").innerHTML=0;
	document.getElementById("loadCount").innerHTML=0;
	document.getElementById("transCount").innerHTML=0;
	document.getElementById("branchCount").innerHTML=0;
}
