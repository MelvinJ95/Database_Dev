angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope', '$location','$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
        var hasliked = false; 
        var hasDisliked = false;  
        var user = 0;

        this.messageList = [];
        this.userList = [];
        this.counter  = 2;
        this.newText = ""; 
        this.hashTag = "";
        this.im = "";
        

        $scope.count_like = 0; 
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

            if(this.im="") {
                var image = null
                console.log('the image is null')
            }
            else{
                console.log('the image is not null')
                console.log(image)
                var fs = require('fs');
                fs.createReadStream(this.im).pipe(fs.createWriteStream('/static'));
            }
            $http.post(url_post,{pcaption: msg, pdate: today, pmedia:image, uid: $routeParams.uid, cid: $routeParams.cid }).then(
                function(response){
                    console.log("data: " + JSON.stringify(response.data));
                
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


        this.update_like = function(index,pid, user){
        
            if($routeParams.uid == user && hasliked){ //user already hit like 
                thisCtrl.messageList[index].like -= 1;
                this.deleteLike_Dislike($routeParams.uid, pid); 
                hasliked = false; 
             }
             else{
                thisCtrl.messageList[index].like += 1;
                this.insertLike_Dislike("like",pid);
                hasliked = true; 
             }
    
    
        };

    
        this.update_dislike = function(index,pid, user){
        
            if($routeParams.uid == user && hasDisliked){ //user already hit like 
                thisCtrl.messageList[index].dislike -= 1;
                this.deleteLike_Dislike($routeParams.uid, pid); 
                hasDisliked = false; 
             }
             else{
                thisCtrl.messageList[index].dislike += 1;
                this.insertLike_Dislike("dislike",pid);
                hasDisliked = true; 
             }
    
    
        };

        this.like= function(index,pid){ //DOesn't work when clicking like consecutively on different posts each time 
        console.log("ENTERED LIKE FUNCTION");
        console.log(hasliked);
       var url = "http://127.0.0.1:5000/GramChat/users/reaction/like/"+pid;
       $http.get(url).then(
         function(response){
             console.log("Response: "+JSON.stringify(response));
             thisCtrl.userList = response.data.Users;
             for(var i=0;i<thisCtrl.userList.length;i++){
                 if($routeParams.uid == thisCtrl.userList[i].uid){
                    user = thisCtrl.userList[i].uid; 
                    thisCtrl.update_like(index,pid,user);
                 }
             }
             console.log("INSIDE"+user);
         },

         function (response){
            thisCtrl.update_like(index,pid,user);
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
                return; 
             }
             
         });
    
        };


     this.dislike= function(index,pid){ //DOesn't work when clicking like consecutively on different posts each time 
        console.log("ENTERED DISLIKE FUNCTION");

       var url = "http://127.0.0.1:5000/GramChat/users/reaction/dislike/"+pid;
       $http.get(url).then(
         function(response){
             console.log("Response: "+JSON.stringify(response));
             thisCtrl.userList = response.data.Users;
             for(var i=0;i<thisCtrl.userList.length;i++){
                 if($routeParams.uid == thisCtrl.userList[i].uid){
                     user = thisCtrl.userList[i].uid; 
                     thisCtrl.update_dislike(index,pid,user);
                 }
             }
         },
         function (response){
             thisCtrl.update_dislike(index,pid,user);
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
                return; 
             }
         });
        };    

   

        this.insertLike_Dislike = function(reaction,pid){
        var url_post = "http://127.0.0.1:5000/GramChat/reactions";
        var today = new Date();
        var dd = today.getDate();
        var mm = today.getMonth()+1; //January is 0!
        var yyyy = today.getFullYear();
        today = dd + '-' + mm + '-' + yyyy;
        $http.post(url_post,{rdate:today,reaction:reaction,pid:pid,uid:$routeParams.uid }).then(
            function(response){
                console.log("data: " + JSON.stringify(response.data));
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

        this.deleteLike_Dislike = function(uid,pid){
        var empty = {};
            
        var reqURL = "http://localhost:5000/GramChat/reactions/delete/"+uid+"/"+pid;
        console.log("reqURL: " + reqURL);

        $http.delete(reqURL,empty).then(
            function(response){
                console.log("data: " + JSON.stringify(response.data));
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

    // this.addImage = function(path) {
    //
    //
    // };

    this.viewReaction = function(mid){
         $location.path('/likes/' + mid);
    };
    this.goHome = function(){
        
	    $location.path('/main/'+$routeParams.uid);
	};
        this.loadMessages();
}]);
