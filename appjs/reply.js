angular.module('AppChat').controller('ReplyController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
        this.Message = "";
        var list = [];
        this.mid;
        this.cid;
        this.uid;
        this.disp;

         this.loadReplies = function(){
              //var list = [];
              thisCtrl.cid = $routeParams.cid;
              thisCtrl.uid = $routeParams.uid;
              thisCtrl.mid = $routeParams.mid;
              var url = "http://127.0.0.1:5000/GramChat/posts/reply/"+thisCtrl.mid;
              $http.get(url).then(
                function(response){
                    console.log("Response: "+JSON.stringify(response));
                    thisCtrl.list = response.data.Replies

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

            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.list));
            console.log(list);
        };
         this.postReply = function(){
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

            var url_post = "http://127.0.0.1:5000/GramChat/chat/reply/" + thisCtrl.mid;

            $http.post(url_post,{pcaption: msg, pdate: today, pmedia:null, uid: $routeParams.uid, cid: $routeParams.cid }).then(
                function(response){
                    console.log("data: " + JSON.stringify(response.data));
                    thisCtrl.returnToReplies();
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

        // this.postReply = function(){
        //     var reqURL = "http://localhost:5000/GramChat/chat/reply/" + thisCtrl.mid;
        //     console.log("reqURL: " + reqURL);
        //     var empty = {};
        //     $http.post(reqURL,empty).then(
        //         function(response){
        //             console.log("data: " + JSON.stringify(response.data));
        //             thisCtrl.returnToChat();
        //         },
        //         function(response){
        //             var status = response.status;
        //
        //             if (status == 0){
        //                 alert("No internet connection");
        //             }
        //             else if (status == 401){
        //                 alert("Session has expired");
        //             }
        //             else if (status == 403){
        //                 alert("Authorization required");
        //             }
        //             else if (status == 404){
        //                 alert("Page not found");
        //             }
        //             else {
        //                 alert("Internal system error has occurred");
        //             }
        //         }
        //     );
        // };

	this.returnToChat = function(){
		$location.url('/chat/'+ thisCtrl.cid + '/' + thisCtrl.uid);
	};

	this.returnToReplies = function(){
        $location.url('/reply/'+ thisCtrl.cid + '/' + thisCtrl.uid + '/' + thisCtrl.mid);
    };

	this.loadVar = function(){
		thisCtrl.mid = $routeParams.mid;
		thisCtrl.cid = $routeParams.cid;
		thisCtrl.uid = $routeParams.uid;
		thisCtrl.disp = $routeParams.disp;
		
	};
        this.loadReplies();
        this.loadVar();
}]);
