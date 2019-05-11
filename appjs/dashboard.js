angular.module('AppChat').controller('DashboardController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
    var thisCtrl = this;
        var hasliked = false;
        var hasDisliked = false;
        var user = 0;

        this.pList = [];
        this.userList = [];
        this.counter  = 2;
        this.newText = "";
        this.hashTag = "";

    this.loadP = function(){

              thisCtrl.cid = $routeParams.cid;
              thisCtrl.uid = $routeParams.uid;
              var url = "http://127.0.0.1:5000/GramChat/postsperday";
              $http.get(url).then(
                function(response){
                    console.log("Response: "+JSON.stringify(response));
                    thisCtrl.pList = response.data.Posts

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

            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.pList));
        };











//     var url = "http://127.0.0.1:5000/GramChat/postsperday";
//     var list = [];
//     $http.get(url).then(
//                 function(response) {
//                    console.log(JSON.stringify(response));
//                    var list2 = JSON.stringify(response);
//                     list = response.data.Replies;
//                     var chart = c3.generate({
//                      data: {
//                          columns: list2.search('total'),
//                          rows: list2.search('date')
//                      }
//     } );
//
//                     return list2;
//                 });
//
//     console.log();
//         console.log(d3.json(url));
// //      var chart = c3.generate({
// //     data: {
// //         // columns: [
// //         //     ['data1', 30, 200, 100, 400, 150, 250],
// //         //     ['data2', 50, 20, 10, 40, 15, 25]
// //         // ]
// //         json: 'http://127.0.0.1:5000/GramChat/postsperday'
// //         // type: 'json'
// //         //json: JSON.parse('http://127.0.0.1:5000/GramChat/posts')
// //         // type: 'line'
// //
// //     }
// // }
// // );
//
// // setTimeout(function () {
// //     chart.load({
// //         columns: [
// //             ['data1', 230, 190, 300, 500, 300, 400]
// //         ]
// //     });
// // }, 1000);
// //
// // setTimeout(function () {
// //     chart.load({
// //         columns: [
// //             ['data3', 130, 150, 200, 300, 200, 100]
// //         ]
// //     });
// // }, 1500);
// //
// // setTimeout(function () {
// //     chart.unload({
// //         ids: 'data1'
// //     });
// // }, 2000);

        this.loadP();
}]);
//
// ]);