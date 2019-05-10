angular.module('AppChat').controller('removeParticipantController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
	this.user;
    this.uid;
    this.cid;


        this.removeMember = function(id){
            var empty = {};
            
            var reqURL = "http://localhost:5000/GramChat/chat/removeUser/"+thisCtrl.cid+"/"+id;
            console.log("reqURL: " + reqURL);

            $http.delete(reqURL,empty).then(
                function(response){
                    console.log("data: " + JSON.stringify(response.data));
 		            thisCtrl.goToChatPage();
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
        }

        this.load = function(){

            console.log("Using dispname: " + thisCtrl.uid);
            var url = "http://localhost:5000/GramChat/chat/members/"+thisCtrl.cid;
            $http.get(url).then(
                function (response){
                    console.log("response: " + JSON.stringify(response));
                    thisCtrl.contactList = response.data.Users;
                    $log.error("Contacts Loaded: ", JSON.stringify(thisCtrl.contactList));

                }, // error callback
                function (response){
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
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
	
    }
        this.goToChatPage = function(){
            console.log("Moving to main page.");
            $location.path('/chat/'+thisCtrl.cid+'/'+thisCtrl.uid);
        }

        this.loadVar = function(){
        thisCtrl.uid = $routeParams.uid;
        thisCtrl.cid = $routeParams.cid;
        }

	this.loadVar();
	this.load();
        //this.loadMessageDetails();
}]);
