angular.module('AppChat').controller('removeContactController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
	this.user;
    this.first_name = "";
	this.last_name = "";
	this.uid;
	this.phone = "";
	this.email = "";

        this.removeContact = function(id){
            var empty = {};
            
            var reqURL = "http://localhost:5000/GramChat/contacts/removeContact/"+thisCtrl.uid+"/"+id;
            console.log("reqURL: " + reqURL);

            $http.delete(reqURL,{ first_name: thisCtrl.first_name,last_name: thisCtrl.last_name, uemail: thisCtrl.email, uphone: thisCtrl.phone }).then(
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

            console.log("Using dispname: " + thisCtrl.uid);
            var url = "http://localhost:5000/GramChat/contacts/"+thisCtrl.uid;
            $http.get(url).then(
                function (response){
                    console.log("response: " + JSON.stringify(response));
                    thisCtrl.contactList = response.data.Contacts;
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
