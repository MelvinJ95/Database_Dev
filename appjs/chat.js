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
                        return;
                    }
                    else {
                        alert("Internal system error has occurred");
                    }
                });

            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };

        this.postMsg = function(){
            var msg = thisCtrl.newText;

            var author = "";
            var user;
            var name=""; 
            var url = "http://127.0.0.1:5000/GramChat/users/"+$routeParams.uid;
            $http.get(url).then(
                function(response){
                    console.log("Response: "+JSON.stringify(response));
                    user = response.data.User;
                    name = user.first_name;
                    author = name; 
                    var nextId = thisCtrl.counter++;    
                    thisCtrl.messageList.unshift({"id": nextId, "pcaption" : msg, "user" : author, "like" : 0, "dislike" : 0});
                    thisCtrl.newText = "";
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
                        return;
                    }
                    else {
                        alert("Internal system error has occurred");
                    }
                });

            var today = new Date();
            var dd = today.getDate();
            var mm = today.getMonth()+1; //January is 0!
            var yyyy = today.getFullYear();
            today = dd + '-' + mm + '-' + yyyy;

            var url_post = "http://127.0.0.1:5000/GramChat/posts";
            
            $http.post(url_post,{pcaption: msg, pdate: today, pmedia:null, uid: $routeParams.uid, cid: $routeParams.cid }).then(
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
                        return;
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
    
    this.replyToMessage = function(mid){
	    $location.path('/reply/' + thisCtrl.uid + '/' + thisCtrl.cid + '/' + mid);
	};

    this.viewReaction = function(mid){
         $location.path('/likes/' + mid);
    };
    this.goHome = function(){
        
	    $location.path('/main/'+$routeParams.uid);
	};
        this.loadMessages();
}]);
