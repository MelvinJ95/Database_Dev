angular.module('AppChat').controller('SearchController', ['$http', '$log', '$location', '$scope', '$window',
    function($http, $log, $scope) {
        var mem = sessionStorage;
        var thisCtrl = this;

        this.msgHW = [];
        this.messageList = [];
        this.cid = mem.getItem('cid');
        this.hashname = "";

        this.searchhash = function(){
            thisCtrl.loadMessage().then(function(response){
                console.log(response.data);
                thisCtrl.msgHW = response.data.SearchHash;
                console.log(thisCtrl.msgHW);
                console.log(thisCtrl.msgHW[0])
                var n=thisCtrl.msgHW.length;
                for(var i=n-1; i>=0; i--){
                    thisCtrl.messageList.push({"mid": thisCtrl.msgHW[i].MessageID, "text": thisCtrl.msgHW[i].Message, "author": thisCtrl.msgHW[i].Username});
                }

            }, function(error){
                var status = error.status;
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
            this.hashname = ""
            $log.error("Loaded: ", JSON.stringify(thisCtrl.postList));
        };

        this.loadMessage = function(){
            var url = "http://localhost:5000/GramChat/getHashtags/" + thisCtrl.cid +"/" +thisCtrl.hashname;
            console.log(url);
            return $http.get(url)
        };

        this.searchhash();

}]);