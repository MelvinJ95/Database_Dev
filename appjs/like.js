(function () {
    'use strict';
angular.module('AppChat').controller('LikesController', ['$http', '$log', '$scope', '$location','$routeParams',
    function($http, $log, $scope, $location, $routeParams) {

        var thisCtrl = this;
        this.counter  = 2;
        this.newText = "";
        this.postList = [];
        this.showLikes = function(){
            thisCtrl.pid = $routeParams.pid;
            var url = "http://localhost:5000/GramChat/users/reaction/like/" + thisCtrl.pid;
            $http.get(url).then( // success call back
                function (response){
                    console.log("data: " + JSON.stringify(response.data));
                     //*** MISSING response.data TYPE ***\\
                    thisCtrl.postList = response.data.Reactions
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

    this.react = function () {
        var today = new Date();
        var dd = today.getDate();
        var mm = today.getMonth()+1; //January is 0!
        var yyyy = today.getFullYear();
        today = dd + '-' + mm + '-' + yyyy;
        console.log("Hi");
        var url = "http://localhost:5000/GramChat/posts/" + thisCtrl.pid + "/like";

        thisCtrl.pid = $routeParams.pid;
        thisCtrl.uid = $routeParams.uid;

        $http.post(url,{rdate: today, reaction: "like", pid: $routeParams.pid, uid: $routeParams.uid }).then(
            function(response){
                console.log("data: " + JSON.stringify(response.data));
                thisCtrl.returnToMainPage();
            },
            function(response){
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
            }
        );
    };

        this.showLikes();
}])})();
