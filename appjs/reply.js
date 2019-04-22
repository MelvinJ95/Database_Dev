angular.module('AppChat').controller('ReplyController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
        this.Message = "	Enter Reply";
	this.Or_msg_ID;
	this.groupid;
	this.userid;
	this.disp;

        this.postReply = function(){
            var reqURL = "http://localhost:5000/GramChat/GroupChat/Messages/Reply?Or_msg_ID=" + thisCtrl.Or_msg_ID + "&Message=" + thisCtrl.Message + "&UID=" + thisCtrl.userid + "&GID=" + thisCtrl.groupid;
            console.log("reqURL: " + reqURL);
	    var empty = {};
            $http.post(reqURL,empty).then(
                function(response){
                    console.log("data: " + JSON.stringify(response.data));
                    thisCtrl.returnToChat();
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

	this.returnToChat = function(){
		$location.url('/chat/'+ thisCtrl.disp + '/' + thisCtrl.groupid);
	}

	this.loadVar = function(){
		thisCtrl.Or_msg_ID = $routeParams.mid;
		thisCtrl.groupid = $routeParams.gid;
		thisCtrl.userid = $routeParams.uid;
		thisCtrl.disp = $routeParams.disp;
		
	}

        this.loadVar();
}]);