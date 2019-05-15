angular.module('AppChat').controller('AddChatController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
	this.disp;
	this.userid;
	this.cname = ""

        this.addChatGroup = function(){
            var reqURL = "http://localhost:5000/GramChat/chat/createchat";
            console.log("reqURL: " + reqURL);
            console.log("UID: "+thisCtrl.uid);
            $http.post(reqURL,{cname: thisCtrl.cname, uid: thisCtrl.uid}).then(
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
		$location.path('/main/'+ thisCtrl.uid);
	};

	this.loadUID = function(){
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
	};

	this.loadVar = function(){
		thisCtrl.uid = $routeParams.uid;
		
	};

        this.loadVar();
	this.loadUID();
}]);
