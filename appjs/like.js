angular.module('AppChat').controller('LikesController', ['$http', '$log', '$scope', '$rootScope', '$location','$routeParams',
    function($http, $log, $scope, $location, $routeParams)  {

        var thisCtrl = this;
        this.pid;
	    this.cid;
	    this.uid;
	    this.react;
	    this.date;
        this.showLikes = function(){
            thisCtrl.pid = $routeParams.pid;
            var url = "http://localhost:5000/GramChat/reactions/getLikes/" + thisCtrl.pid;
            $http.get(url).then( // success call back
                function (response){
                    console.log("data: " + JSON.stringify(response));
                    thisCtrl.reactList = response.data.Reactions
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

             $log.error("Posts Loaded: ", JSON.stringify(thisCtrl.reactList));
        };

        this.goHome = function(){

	    $location.path('/main/'+$routeParams.uid);
	    };

        this.loadVar = function(){
		    thisCtrl.pid = $routeParams.pid;
		    thisCtrl.cid = $routeParams.cid;
		    thisCtrl.uid = $routeParams.uid;
		    thisCtrl.react = $routeParams.react;
		    thisCtrl.date = $routeParams.date;
	    };

        this.showLikes();
}]);
