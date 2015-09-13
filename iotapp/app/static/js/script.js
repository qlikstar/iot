
// Add your javascript here
   $(function() {
      $("#header").load("html/header.html");
      $("#footer").load("html/footer.html");
    });
    
  
  var piApp = angular.module('piApp', []);
  
   piApp.config(function ($routeProvider){
    $routeProvider
      .when('/', {
        controller : 'DataController',
        templateUrl : 'html/page1.html'
      })
      .when('/addnew', {
        controller : 'DataController',
        templateUrl : 'html/page2.html'
      })
      .otherwise ({ redirectTo : '/'});
    
  });
  
  // var controllers = {};
  
  piApp.controller('DataController', function($scope, $http){
    $scope.data = 
      [{'name' :'Sanket', 'city':'San Francisco' } , 
      {'name' :'Chris', 'city':'San Mateo' },
      {'name' :'Matt', 'city':'Phoenix' }];
     
    //$scope.ledstatus = {led : 'OFF'};
      
    $scope.getLedStatus = function() {
        $http.get('/toggle').
            success(function(data, status, headers, config) {
            $scope.ledstatus = data;
            //console.log(data);
        }).
        error(function(data, status, headers, config) {
            console.log(status);
        });
    };
    //initial load
    $scope.getLedStatus();  
      
    $scope.addPerson = function(){
        $scope.data.push({ name : $scope.personname , city : $scope.personcity });
        $scope.personname = '';
        $scope.personcity = '';
      
    };
      
  });


//   $scope.getLedStatus = function($scope, $http) {
//        $http.get('http://localhost:8080/toggle').
//        success(function(data, status, headers, config) {
//          //$scope.led = data;
//          console.log(status);
//        }).
//        error(function(data, status, headers, config) {
//          // log error
//        });
//    }
  
  
  // controllers.DataController = function($scope){
  //   $scope.data = 
  //     [{'name' :'Sanket', 'city':'San Francisco' } , 
  //     {'name' :'Chris', 'city':'San Mateo' },
  //     {'name' :'Matt', 'city':'Phoenix' }];
  // };
  
  // piApp.controller(controllers);
  
 
  
  

  
