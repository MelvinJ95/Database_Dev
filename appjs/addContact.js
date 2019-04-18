angular.module('AppChat').controller('AddContactController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
	this.disp;
        this.UFirst_name = "     Enter Contact's First Name";
	this.ULast_name = "     Enter Contact's Last Name";
	this.UID;
	this.UPhone = "     Enter Contact's Phone Number";
	this.UEmail = "     Enter Contact's Email";

        this.addNewContact = function(){
            var empty = {};
            
            var reqURL = "http://localhost:5000/GramChat/AddContact?UID="+thisCtrl.UID+"&UFirst_name="+thisCtrl.UFirst_name+"&ULast_name="+thisCtrl.ULast_name+"&UPhone="+thisCtrl.UPhone+"&UEmail="+thisCtrl.UEmail;
            console.log("reqURL: " + reqURL);

            $http.post(reqURL,empty).then(
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

	this.loadUID = function(){
	    var author = thisCtrl.disp;
	    var UserInfo;
	    var UserID = 0;
	    console.log("Using dispname: " + thisCtrl.disp);
  	    var url = "http://localhost:5000/GramChat/Users/Username/"+ author;
            $http.get(url).then(
                function (response){
                    console.log("response: " + JSON.stringify(response));
                    UserInfo = response.data.Users;
                    $log.error("The User Loaded: ", UserInfo);
		    $log.error("User ID: ", UserInfo[0].UID);
		    UserID = UserInfo[0].UID;
		    thisCtrl.UID = UserID;
		    console.log("Registered ID: " + thisCtrl.UID);

            }, // error callback
            function (response){
                // This is the error function
                // If we get here, some error occurred.
                // Verify which was the cause and show an alert.
                var status = response.status;
                if (status == 0){
                    alert("No hay conexion a Internet");
                }
                else if (status == 401){
                    alert("Su sesion expiro. Conectese de nuevo.");
                }		
                else if (status == 403){
                    alert("No esta autorizado a usar el sistema.");
                }
                else if (status == 404){
                    alert("No se encontro la informacion solicitada.");
                }
                else {
                    alert("Error interno del sistema.");
                }
            });
	}

        this.goToMainPage = function(){
            console.log("Moving to main page.");
            $location.url('/mainpage/'+thisCtrl.disp);
        }

        this.loadVar = function(){
	    thisCtrl.disp = $routeParams.disp;
        }

	this.loadVar();
	this.loadUID();
        //this.loadMessageDetails();
}]);
