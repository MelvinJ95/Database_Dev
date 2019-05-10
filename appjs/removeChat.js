angular.module('AppChat').controller('removeChatController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
        this.user;
        this.uid;
        this.cid;

        this.removeChat = function(id){
            var empty = {};

            var reqURL = "http://localhost:5000/GramChat/chat/delete/" + id + '/' + thisCtrl.uid;
            console.log("reqURL: " + reqURL);

            $http.delete(reqURL,empty).then(
                function(response){
                    console.log("data: " + JSON.stringify(response.data));
 		            thisCtrl.goToMainPage();
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

        this.load = function(){
            thisCtrl.uid = $routeParams.uid;

            var reqURL = "http://localhost:5000/GramChat/users/chats/" + thisCtrl.uid;
            console.log("reqURL: " + reqURL);

            $http.get(reqURL).then(
                function(response){
                    console.log("data: " + JSON.stringify(response.data));
                    thisCtrl.grouplist = response.data.Chats;
		    $log.error("GroupChats Loaded: ", JSON.stringify(thisCtrl.grouplist));
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

        this.goToMainPage = function(){
            console.log("Moving to main page.");
            $location.url('/main/'+thisCtrl.uid);
        };

        this.loadVar = function(){
	    thisCtrl.uid = $routeParams.uid;
        };

	this.loadVar();
	this.load();
        //this.loadMessageDetails();
}]);
