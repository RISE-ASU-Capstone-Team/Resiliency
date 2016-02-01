var clientApp = angular.module('clientApp', []);

clientApp.controller('PowerDetailController',
    ['$scope', '$http', function($scope, $http){
        $http.get('http://localhost:8000/power/api/power/1'
            + '/?format=json').success(function(data){
            $scope.power = data;
            console.log($scope.power.name);
        })
    }
]);