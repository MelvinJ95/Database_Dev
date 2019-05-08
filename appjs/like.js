angular.module('AppChat').controller('LikesController', ['$http', '$log', '$scope', '$rootScope', '$location','$routeParams',
    function($http, $log, $scope, $rootScope, $location,$routeParams)  {

        var thisCtrl = this;
        this.counter  = 2;
        this.newText = "";
        this.showLikes = function(){
            thisCtrl.pid = $routeParams.pid;
            var url = "http://localhost:5000/GramChat/reactions/getLikes/" + thisCtrl.pid;
            $http.get(url).then( // success call back
                function (response){
                    console.log("data: " + JSON.stringify(response.data));
                     //*** MISSING response.data TYPE ***\\
                    thisCtrl.postList = response.data
            }, // error callback
            function (response){
                console.log("Error response: " + JSON.stringify(response));
                var status = response.status;
                if (status == 0){
                    alert("No internet connection");
                }
                else if (status == 401){
                    alert("Session has expired");
                }
                else if (status == 403){
                    alert("Authorization required");
                }
                else if (status == 404){
                    alert("Page not found");
                }
                else {
                    alert("Internal system error has occurred");
                }
            });

             $log.error("Posts Loaded: ", JSON.stringify(thisCtrl.postList));
        };

        this.goHome = function(){

	    $location.path('/main/'+$routeParams.uid);
	};

        this.showLikes();
}]);
