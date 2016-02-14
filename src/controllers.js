/*
var powerControllers = angular.module('powerControllers', []);

powerControllers.controller('PowerDetailController',
    ['$scope', '$routParams', '$http', function($scope, $routParams, $http){
        $http.get('http://localhost:8000/power/api/power/' + $routParams.powerId
                + '/?format=json').success(function(data){
            $scope.power = data;
        })
    }
]);
*/