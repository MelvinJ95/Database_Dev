angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope', '$location','$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;

        this.messageList = [];
        this.counter  = 2;
        this.newText = ""; 
        this.hashTag = "";

        this.loadMessages = function(){
  
              thisCtrl.cid = $routeParams.cid;
              thisCtrl.uid = $routeParams.uid;
              var url = "http://127.0.0.1:5000/GramChat/posts/chat/"+thisCtrl.cid;
              $http.get(url).then(
                function(response){
                    console.log("Response: "+JSON.stringify(response));
                    thisCtrl.messageList = response.data.Posts

                },
                function (response){
                    console.log("Error response: "+JSON.stringify(response));
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
                        continue;
                    }
                    else {
                        alert("Internal system error has occurred");
                    }
                });

            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };

        this.postMsg = function(){
            var msg = thisCtrl.newText;
            // Need to figure out who I am
            var author = "Me";
            var nextId = thisCtrl.counter++;
            thisCtrl.messageList.unshift({"id": nextId, "pcaption" : msg, "user" : author, "like" : 0, "dislike" : 0});
            thisCtrl.newText = "";
        };

        this.loadMessagesByHashtag = function(){
              thisCtrl.cid = $routeParams.cid;
              thisCtrl.uid = $routeParams.uid;
              var url = "http://127.0.0.1:5000/GramChat/chat/"+thisCtrl.cid+"/posts/hashtag/"+thisCtrl.hashTag;
              $http.get(url).then(
                function(response){
                    console.log("Response: "+JSON.stringify(response));
                    thisCtrl.messageList = response.data.Posts

                },
                function (response){
                    console.log("Error response: "+JSON.stringify(response));
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
                        continue;
                    }
                    else {
                        alert("Internal system error has occurred");
                    }
                });

            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };

    this.goToAddParticipant = function(){
        thisCtrl.cid = $routeParams.cid;
        thisCtrl.uid = $routeParams.uid;
	    $location.path('/addParticipant/'+thisCtrl.cid+'/'+thisCtrl.uid);
	};

    this.goToRemoveParticipant = function(){
        thisCtrl.cid = $routeParams.cid;
        thisCtrl.uid = $routeParams.uid;
	    $location.path('/removeParticipant/'+thisCtrl.cid+'/'+thisCtrl.uid);
	};

    this.goHome = function(){
        
	    $location.path('/main/'+$routeParams.uid);
	};
        this.loadMessages();
}]);
