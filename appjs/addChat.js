angular.module('AppChat').controller('AddChatController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
	this.disp;
	this.userid;
	this.GName = "	Enter Chat Name"

        this.addChatGroup = function(){
            var reqURL = "http://localhost:5000/GramChat/GroupChats?GName="+thisCtrl.GName+"&UID="+thisCtrl.userid;
            console.log("reqURL: " + reqURL);
	    var empty = {};
            $http.post(reqURL,empty).then(
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

	this.returnToMainPage = function(){
		$location.url('/mainpage/'+ thisCtrl.disp);
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
		    thisCtrl.userid = UserID;
		    console.log("Registered ID: " + thisCtrl.userid);

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

	this.loadVar = function(){
		thisCtrl.disp = $routeParams.UDispName;
		
	}

        this.loadVar();
	this.loadUID();
}]);
