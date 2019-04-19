angular.module('AppChat').controller('MainPageController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
	this.grouplist = [];
	this.uid;
        
        this.loadMainPage = function(){
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

	this.goToAddChatPage = function(){
		$location.url('/addChat/'+thisCtrl.uid);
	}
	
	this.goToAddContactPage = function(){
		$location.url('/addContact/'+thisCtrl.uid);
	}

	this.chatpage = function (gid){
	        console.log("Going to message page for group: " + gid);
            $location.url('/chat/' + thisCtrl.uid + '/' + gid);
        }

	this.loadMainPage();
}]);
