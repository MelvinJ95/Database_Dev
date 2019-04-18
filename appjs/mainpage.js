angular.module('AppChat').controller('MainPageController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
	this.grouplist = [];
	this.dispname;
        
        this.loadMainPage = function(){
            thisCtrl.dispname = $routeParams.UDispName;
	
            var reqURL = "http://localhost:5000/GramChat/GroupChats/User/name/" + thisCtrl.dispname;
            console.log("reqURL: " + reqURL);

            $http.get(reqURL).then(
                function(response){
                    console.log("data: " + JSON.stringify(response.data));
                    thisCtrl.grouplist = response.data.GroupChats;
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
		$location.url('/addChat/'+thisCtrl.dispname);
	}
	
	this.goToAddContactPage = function(){
		$location.url('/addContact/'+thisCtrl.dispname);
	}

	this.chatpage = function (gid){
	        console.log("Going to message page for group: " + gid);
            $location.url('/chat/' + thisCtrl.dispname + '/' + gid);
        }

	this.loadMainPage();
}]);
