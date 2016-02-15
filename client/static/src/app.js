var clientApp = angular.module('clientApp', ['ngRoute']);

clientApp.config(function($routeProvider) {
        $routeProvider.
          when('/', {
            templateUrl: 'static/power-list.html',
            controller: 'PowerListController'
          }).
          when('/power/:powerID', {
            templateUrl: 'static/power-detail.html',
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
        })
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