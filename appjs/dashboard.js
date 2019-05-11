angular.module('AppChat').controller('DashboardController', ['$http', '$log', '$scope', '$window',
    function($http, $log, $scope) {
        var url = "http://127.0.0.1:5000/GramChat/postsperday";
        var likesList = {};
        $http.get(url).then(
            function (response) {
                console.log("Response: " + JSON.stringify(response));
                this.likesList = response.data.Likes
                var chart = c3.generate({
                    data: {
                        url: '/static/file.csv',
                        type: 'line'
                    }
                })
            }
        )
    }
]);