var clientApp = angular.module('clientApp', ['ngRoute']);

clientApp.config(function($routeProvider) {
        $routeProvider.
          when('/', {
            templateUrl: 'static/power-list.html',
            controller: 'PowerListController'
          }).
          when('/power/:powerID', {
            templateUrl: 'static/power-list.html',
            controller: 'PowerDetailController'
          }).
          otherwise({
            redirectTo: '/'
          });
      });

clientApp.controller('PowerListController',
    ['$scope', '$http', '$timeout', '$route', function(scope, http, timeout, route){
        console.log("created");
        http.get('http://localhost:8000/data/api/power'
                 + '/?format=json').success(function(d){
            scope.powerList = d;
        });

        var poll = function() {
            polling = true;
            timeout(function() {
                http.get('http://localhost:8000/data/api/update'
                    + '/?format=json').then(function successCallback(response){
                    if((response.data[0].update_check*1000) > (new Date).getTime()-5000){
                        http.get('http://localhost:8000/data/api/power'
                                 + '/?format=json').success(function(d){
                            scope.powerList = d;
                            route.reload();
                        })
                    }else{

                    }
                }, function errorCallback(response){
                    console.log("Error retrieving update");
                })
                poll();
            }, 2000);
        };
        if(!polling){
            poll();
        }


        scope.nodeListClicked = function(powerID){
            var data;
            http.get('http://localhost:8000/data/api/power/'
                + powerID + '/?format=json').success(function(d){
                data = d;

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
                    if(keys[i] == 'active'){
                        $('#cmn-toggle-1').prop('checked', data[keys[i]]);
                    }else{
                        td.innerHTML = formatTableName(keys[i]);
                        tr.appendChild(td);
                    }
                    if(i+1 == keys.length){
                        td.style = "padding-bottom: 15px";
                    }
                    td = document.createElement('td');
                    td.className = "rowData";
                    td.onclick = function(e){editComponent(this)};
                    if(keys[i] == 'active'){

                    }else if(keys[i] == 'created_date'){
                        var date = new Date(data[keys[i]]*1000);
                        var day = date.getDate();
                        var monthIndex = date.getMonth();
                        var year = date.getFullYear();

                        td.innerHTML = monthNames[monthIndex] + ' ' + day + ', ' + year;
                    }else{
                        td.innerHTML = data[keys[i]];
                    }
                    tr.appendChild(td);
                    componentTable.tBodies[0].appendChild(tr);
                }
                td.style = "padding-bottom: 15px";
            })
        }
    }
]);

clientApp.controller('PowerDetailController',
    ['$scope', '$http', '$routeParams', function(scope, http, params){
        console.log(params.powerID);
        http.get('http://localhost:8000/data/api/power/'
            + params.powerID + '/?format=json').success(function(data){
            scope.power = data;
        })
    }
]);