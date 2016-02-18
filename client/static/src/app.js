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
    ['$scope', '$http', function(scope, http){
        http.get('http://localhost:8000/data/api/power'
            + '/?format=json').success(function(data){
            scope.powerList = data;
            powerNodes= data;
        })

        scope.nodeListClicked = function(data){
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
                td.innerHTML = formatTableName(keys[i]);
                tr.appendChild(td);
                if(i+1 == keys.length){
                    td.style = "padding-bottom: 15px";
                }
                td = document.createElement('td');
                td.className = "rowData";
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