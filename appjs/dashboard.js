/**
 * Created by manuel on 5/8/18.
 */

angular.module('AppChat').controller('DashboardController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;

// Load the Visualization API and the piechart package.
google.charts.load('current', {'packages': ['corechart', 'bar', 'table', 'linechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawHashtagsChart);
google.charts.setOnLoadCallback(drawPostChart);
google.charts.setOnLoadCallback(drawRepliesChart);
google.charts.setOnLoadCallback(drawLikesChart);
google.charts.setOnLoadCallback(drawDislikesChart);
google.charts.setOnLoadCallback(drawPostUserChart);
google.charts.setOnLoadCallback(drawRepliesPerPostChart);
// google.charts.setOnLoadCallback(drawLikesPerPostChart);
// google.charts.setOnLoadCallback(drawDislikesPerPostChart);
// google.charts.setOnLoadCallback(drawTopThreeActiveUsersChart);

// Hashtags
function reformatHashtagsData(jsonData){
    var temp = jsonData.Trends;
    console.log(temp);
    console.log("temp: " + JSON.stringify(temp));

    var result = [];
    var i;

    for(i=0; i < temp.length && i < 10; i++) {
        dataElement = [];
        dataElement.push(temp[i]["hashtag"]);
        dataElement.push(temp[i]["position"]);
        result.push(dataElement);
    }
    console.log(result);
    return result;
}


function drawHashtagsChart()
{
    var jsonData = $.ajax({
        url: "http://localhost:5000/GramChat/trends",
        dataType: "json",
        async: false
    }).responseText;
    console.log(jsonData);
    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'hashtag');
    data.addColumn('number', 'position');
    data.addRows(reformatHashtagsData(JSON.parse(jsonData)));

    var options = {
        title: 'Trending Hashtags',
        chartArea: {width: '800px'},
        hAxis: {
            title: 'Trending Hashtags',
            minValue: 0
        },
        vAxis: {
            title: 'Hashtag'
        }
    };
    var chart = new google.visualization.LineChart(document.getElementById('trending_hashtags'));
    chart.draw(data, options);
}

// Post
function reformatPostData(jsonData)
{
    var temp = jsonData.Posts;
    console.log(temp);
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    for(i=0; i < temp.length && i < 10; i++) {
        dataElement = [];
        dataElement.push(temp[i]["day"]);
        dataElement.push(temp[i]["posts"]);
        result.push(dataElement);
    }
    console.log(result);
    return result;
}

function drawPostChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/GramChat/postsperday",
        dataType: "json",
        async: false
    }).responseText;
    console.log(jsonData);
    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Days');
    data.addColumn('number', 'Number of Post');
    data.addRows(reformatPostData(JSON.parse(jsonData)));
    var options = {
        title: 'Posts per day',
        chartArea: {width: '800px'},
        hAxis: {
            title: 'Total Posts',
            minValue: 0
        },
        vAxis: {
            title: 'Day'
        }
    };
    var chart = new google.visualization.LineChart(document.getElementById('postPerDay'));
    chart.draw(data, options);
}

//Replies
function reformatRepliesData(jsonData){
    var temp = jsonData.Posts;
    console.log(temp);
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    for(i=0; i < temp.length && i < 10; i++) {
        dataElement = [];
        dataElement.push(temp[i]["date"]);
        dataElement.push(temp[i]["replies"]);
        result.push(dataElement);
    }
    console.log(result);
    return result;
}

function drawRepliesChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/GramChat/replies/date",
        dataType: "json",
        async: false
    }).responseText;
    console.log(jsonData);
    console.log("jsonData: " + JSON.parse(jsonData));
    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Days');
    data.addColumn('number', 'Number of Replies');
    data.addRows(reformatRepliesData(JSON.parse(jsonData)));
    var options = {
        title: 'Replies per day',
        chartArea: {width: '800px'},
        hAxis: {
            title: 'Total Replies',
            minValue: 0
        },
        vAxis: {
            title: 'Day'
        }
    };
    var chart = new google.visualization.LineChart(document.getElementById('repliesPerDay'));
    chart.draw(data, options);
}

//Likes
function reformatLikesData(jsonData){
    var temp = jsonData.Reactions;
    console.log(temp);
    console.log("temp: " + JSON.stringify(temp));

    var result = [];
    var i;

    for(i=0; i < temp.length && i < 10; i++) {
        dataElement = [];
        dataElement.push(temp[i]["date"]);
        dataElement.push(temp[i]["likes"]);
        result.push(dataElement);
    }
    console.log(result);
    return result;
}

function drawLikesChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/GramChat/likes/date",
        dataType: "json",
        async: false
    }).responseText;
    console.log(jsonData);
    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Days');
    data.addColumn('number', 'Number of Likes');
    data.addRows(reformatLikesData(JSON.parse(jsonData)));

    var options = {
        title: 'Likes per day',
        chartArea: {width: '800px'},
        hAxis: {
            title: 'Total Likes',
            minValue: 0
        },
        vAxis: {
            title: 'Day'
        }
    };

    var chart = new google.visualization.LineChart(document.getElementById('likesPerDay'));

    chart.draw(data, options);

}


//Dislikes
function reformatDislikesData(jsonData){
    var temp = jsonData.Reactions;
    console.log(temp);
    console.log("temp: " + JSON.stringify(temp));

    var result = [];
    var i;

    for(i=0; i < temp.length && i < 10; i++) {
        dataElement = [];
        dataElement.push(temp[i]["date"]);
        dataElement.push(temp[i]["dislikes"]);
        result.push(dataElement);
    }
    console.log(result);
    return result;
}


function drawDislikesChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/GramChat/dislikes/date",
        dataType: "json",
        async: false
    }).responseText;
    console.log(jsonData);
    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Days');
    data.addColumn('number', 'Number of Dislikes');
    data.addRows(reformatDislikesData(JSON.parse(jsonData)));

    var options = {
        title: 'Dislikes per day',
        chartArea: {width: '800px'},
        hAxis: {
            title: 'Total Dislikes',
            minValue: 0
        },
        vAxis: {
            title: 'Day'
        }
    };
    var chart = new google.visualization.LineChart(document.getElementById('dislikesPerDay'));
    chart.draw(data, options);
}

// Post per day by some user
function reformatPostUserData(jsonData)
{
    var temp = jsonData.Posts;
    console.log(temp);
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    for(i=0; i < temp.length && i < 10; i++) {
        dataElement = [];
        dataElement.push(temp[i]["day"]);
        dataElement.push(temp[i]["posts"]);
        result.push(dataElement);
    }
    console.log(result);
    return result;
}

function drawPostUserChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/GramChat/posts/date/user/"+ $routeParams.uid,
        dataType: "json",
        async: false
    }).responseText;
    console.log(jsonData);
    console.log($routeParams.uid);
    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Days');
    data.addColumn('number', 'Number of Post');
    data.addRows(reformatPostUserData(JSON.parse(jsonData)));
    var options = {
        title: 'Posts per day by this user',
        chartArea: {width: '800px'},
        hAxis: {
            title: 'Total Posts',
            minValue: 0
        },
        vAxis: {
            title: 'Day'
        }
    };
    var chart = new google.visualization.LineChart(document.getElementById('postPerDayByUser'));
    chart.draw(data, options);
}

//RepliesPerPost
function reformatRepliesPerPostData(jsonData){
    var temp = jsonData.Replies;
    console.log(temp);
    console.log("temp: " + JSON.stringify(temp));

    var result = [];
    var i;

    for(i=0; i < temp.length && i < 10; i++) {
        dataElement = [];
        dataElement.push(temp[i]["post"]);
        dataElement.push(temp[i]["replies"]);
        result.push(dataElement);
    }
    console.log(result);
    return result;
}


function drawRepliesPerPostChart() {
    var jsonData = $.ajax({
        url: "http://127.0.0.1:5000/GramChat/posts/replies",
        dataType: "json",
        async: false
    }).responseText;
    console.log(jsonData);
    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('number', 'Post');
    data.addColumn('number', 'Replies');
    data.addRows(reformatRepliesPerPostData(JSON.parse(jsonData)));

    var options = {
        title: 'Replies Per Post',
        chartArea: {width: '800px'},
        hAxis: {
            title: 'Replies Per Post',
            minValue: 0
        },
        vAxis: {
            title: 'RepliesPerPost'
        }
    };

    var chart = new google.charts.Bar(document.getElementById('repliesPerPost'));

    chart.draw(data, options);

}

// //Likes Per Post
// function reformatLikesPerPostData(jsonData){
//     var temp = jsonData.Reaction;
//     console.log(temp)
//     console.log("temp: " + JSON.stringify(temp));
//
//     var result = [];
//     var i;
//
//     for(i=0; i < temp.length && i < 10; i++) {
//         dataElement = [];
//         dataElement.push(temp[i]["pid"]);
//         dataElement.push(temp[i]["likes"]);
//         result.push(dataElement);
//     }
//     console.log(result);
//     return result;
// }
//
//
// function drawLikesPerPostChart() {
//     var jsonData = $.ajax({
//         url: "http://localhost:5000/chatGroup/Likes/Post",
//         dataType: "json",
//         async: false
//     }).responseText;
//     console.log(jsonData);
//     console.log("jsonData: " + JSON.parse(jsonData));
//     // Create our data table out of JSON data loaded from server.
//     var data = new google.visualization.DataTable();
//     data.addColumn('string', 'post_name');
//     data.addColumn('number', 'total_likes');
//     data.addRows(reformatLikesPerPostData(JSON.parse(jsonData)));
//
//     var options = {
//         title: 'Likes Per Post',
//         chartArea: {width: '800px'},
//         hAxis: {
//             title: 'Likes Per Post',
//             minValue: 0
//         },
//         vAxis: {
//             title: 'LikesPerPost'
//         }
//     };
//     var chart = new google.charts.Bar(document.getElementById('likesPerPost'));
//     chart.draw(data, options);
// }
//
//
// //Dislikes Per Post
// function reformatDislikesPerPostData(jsonData){
//     var temp = jsonData.Dashboard; //aqui va dashboard?
//     console.log(temp)
//     console.log("temp: " + JSON.stringify(temp));
//
//     var result = [];
//     var i;
//
//     for(i=0; i < temp.length && i < 10; i++) {
//         dataElement = [];
//         dataElement.push(temp[i]["post"]);
//         dataElement.push(temp[i]["dislikes"]);
//         result.push(dataElement);
//     }
//     console.log(result);
//     return result;
// }
//
//
// function drawDislikesPerPostChart() {
//     var jsonData = $.ajax({
//         url: "http://localhost:5000/chatGroup/Dislikes/Post",
//         dataType: "json",
//         async: false
//     }).responseText;
//     console.log(jsonData);
//     console.log("jsonData: " + JSON.parse(jsonData));
//
//     // Create our data table out of JSON data loaded from server.
//     var data = new google.visualization.DataTable();
//     data.addColumn('string', 'post_name');
//     data.addColumn('number', 'total_dislikes');
//     data.addRows(reformatDislikesPerPostData(JSON.parse(jsonData)));
//
//     var options = {
//         title: 'Dislikes Per Post',
//         chartArea: {width: '800px'},
//         hAxis: {
//             title: 'Dislikes Per Post',
//             minValue: 0
//         },
//         vAxis: {
//             title: 'DislikesPerPost'
//         }
//     };
//     var chart = new google.charts.Bar(document.getElementById('dislikesPerPost'));
//     chart.draw(data, options);
// }
//
// //TopThreeActiveUsers
// function reformatTopThreeActiveUsersData(jsonData){
//     var temp = jsonData.Dashboard;
//     console.log(temp)
//     console.log("temp: " + JSON.stringify(temp));
//
//     var result = [];
//     var i;
//
//     for(i=0; i < temp.length && i < 10; i++) {
//         dataElement = [];
//         dataElement.push(temp[i]["username"]);
//         dataElement.push(temp[i]["total_posts"]);
//         result.push(dataElement);
//     }
//     console.log(result);
//     return result;
// }
//
//
// function drawTopThreeActiveUsersChart() {
//     var jsonData = $.ajax({
//         url: "http://localhost:5000/chatGroup/Post/Active/User",
//         dataType: "json",
//         async: false
//     }).responseText;
//     console.log(jsonData);
//     console.log("jsonData: " + JSON.parse(jsonData));
//
//     // Create our data table out of JSON data loaded from server.
//     var data = new google.visualization.DataTable();
//     data.addColumn('string', 'username');
//     data.addColumn('number', 'activity');
//     data.addRows(reformatTopThreeActiveUsersData(JSON.parse(jsonData)));
//
//     var options = {
//         title: 'TopThreeActiveUsers',
//         chartArea: {width: '800px'},
//         hAxis: {
//             title: 'TopThreeActiveUsers',
//             minValue: 0
//         },
//         vAxis: {
//             title: 'TopThreeActiveUsers'
//         }
//     };
//     var chart = new google.charts.Bar(document.getElementById('topThreeActiveUsers'));
//     chart.draw(data, options);
// }
        this.goHome = function(){
            thisCtrl.uid = $routeParams.uid;
            $location.path('/main/'+$routeParams.uid);
    };
}]);