angular.module('AppChat').controller('AddContactController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
	this.user;
    this.first_name = "";
	this.last_name = "";
	this.uid;
	this.phone = "";
	this.email = "";

        this.addNewContact = function(){
            var empty = {};
            
            var reqURL = "http://localhost:5000/GramChat/contacts/addContact/"+thisCtrl.uid;
            console.log("reqURL: " + reqURL);

            $http.post(reqURL,{ first_name: thisCtrl.first_name,last_name: thisCtrl.last_name, uemail: thisCtrl.email, uphone: thisCtrl.phone }).then(
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
        }

        this.load = function(){
            var user = thisCtrl.uid;
            var UserInfo;
            var UserID = 0;
            console.log("Using dispname: " + thisCtrl.uid);
              var url = "http://localhost:5000/GramChat/users/"+ user;
                $http.get(url).then(
                    function (response){
                        console.log("response: " + JSON.stringify(response));
                        UserInfo = response.data.Users;
                        $log.error("The User Loaded: ", UserInfo);
                $log.error("User ID: ", UserInfo[0].UID);
                UserID = UserInfo[0].UID;
                thisCtrl.userid = UserID;
                console.log("Registered ID: " + thisCtrl.userid);
    
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
        this.goToMainPage = function(){
            console.log("Moving to main page.");
            $location.url('/main/'+thisCtrl.uid);
        }

        this.loadVar = function(){
	    thisCtrl.uid = $routeParams.uid;
        }

	this.loadVar();
	this.load();
        //this.loadMessageDetails();
}]);
