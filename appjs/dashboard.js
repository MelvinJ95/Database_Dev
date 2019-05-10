angular.module('AppChat').controller('DashboardController', ['$http', '$log', '$scope', '$window',
    function($http, $log, $scope) {
        google.charts.load('current', {packages: ['corechart', 'bar']});
        google.charts.setOnLoadCallback(drawChart('users'));
        google.charts.setOnLoadCallback(drawChart('hashtags'));
        google.charts.setOnLoadCallback(drawChart('activity'));


        function format(jsonData, trendType) {
            var temp;
            if (trendType == 'users'){
                temp = jsonData.Dashboard.TrendingUsers;
            }
            else if (trendType == 'hashtags'){
                temp = jsonData.Dashboard.TrendingHash;

            }
            var result = [];
            var i;
            var row;
            for (i = 0; i < temp.length; ++i) {
                row = temp[i]
                var dataElement = [];
                dataElement.push(row.Name);
                dataElement.push(row.Count);
                result.push(dataElement);
            }
            return result;
        }

        function format2(jsonData) {
            var temp = jsonData.Dashboard;
            console.log("temp: " + JSON.stringify(temp));
            var result = [];
            result.push(["Messages", temp.NumberOfMessages]);
            result.push(["Replies", temp.NumberOfReplies]);
            result.push(["Dislikes", temp.NumberOfDislikes]);
            result.push(["Likes", temp.NumberOfLikes]);
            console.log("Data: " + JSON.stringify(result));
            return result;
        }

        function drawChart(trendtype) {
            var jsonData = $.ajax({
                url: "http://localhost:5000/GramChat/dashboard",
                dataType: "json",
                async: false
            }).responseText;

            var data = new google.visualization.DataTable();
            var id
            if(trendtype=='hashtags'){
                data.addColumn('string', 'Trend Hashtag');
                data.addColumn('number', 'Message number');
                data.addRows(format(JSON.parse(jsonData), trendtype));
                id = 'chart_div'
            }
            else if (trendtype=='users'){
                data.addColumn('string', 'Trend User');
                data.addColumn('number', 'Message number');
                data.addRows(format(JSON.parse(jsonData), trendtype));
                id = 'chart_div2'
            }
            else if (trendtype=='activity'){
                 data.addColumn('string', 'Action');
                 data.addColumn('number', 'Number Of Actions');
                 data.addRows(format2(JSON.parse(jsonData)));
                 id = 'chart_div3'
            }

            if(trendtype=='users'||trendtype=='hashtags'){
                var options = {
                title: 'Top 10 Trending :'+trendtype,
                chartArea: {width: '50%'},
                hAxis: {
                    title: 'Total Number',
                    minValue: 0
                },
                vAxis: {
                    title: 'Trending '+trendtype
                    }
                };
            }
            else if(trendtype=='activity'){
                var options = {
                title: 'Actions Statistics:',
                chartArea: {width: '50%'},
                hAxis: {
                    title: 'Number of Activities',
                    minValue: 0
                },
                vAxis: {
                    title: 'Activities'
                    }
                };
            }
            var chart = new google.visualization.PieChart(document.getElementById(id));
            chart.draw(data, options);
        }
    }
]);