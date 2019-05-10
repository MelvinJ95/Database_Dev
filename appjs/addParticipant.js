angular.module('AppChat').controller('AddParticipantController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
	this.groupid;
	this.userid;
	this.disp;
	this.contactList = [];


	this.loadContacts = function(){
		var url = "http://localhost:5000/GramChat/contacts/"+thisCtrl.uid;
            $http.get(url).then(
                function (response){
                    console.log("response: " + JSON.stringify(response));
                    thisCtrl.contactList = response.data.Contacts;
                    $log.error("Contacts Loaded: ", JSON.stringify(thisCtrl.contactList));

            }, // error callback
            function (response){
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

        this.addParticipant = function(id){
            var empty = {};
            var url = "http://localhost:5000/GramChat/chat/adduser/"+thisCtrl.cid+"/"+id;
            console.log("reqURL: " + url);

            $http.post(url,empty).then(
                function(response){
                    console.log("data: " + JSON.stringify(response.data));
                    thisCtrl.returnToChatPage();
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
		});
        }

        this.returnToChatPage = function(){
            console.log("Moving to chat page.");
            $location.path('/chat/'+thisCtrl.cid+'/'+thisCtrl.uid);
        }


	this.loadVar = function(){
		thisCtrl.cid = $routeParams.cid;
		thisCtrl.uid = $routeParams.uid;
	
		
	}

	this.loadVar();
	this.loadContacts();
}]);
