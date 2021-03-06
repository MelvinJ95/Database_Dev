(function () {
    'use strict';

    angular
        .module('AppChat', ['ngRoute', 'ngCookies'])
        .config(config)
        .run(run);

    config.$inject = ['$routeProvider', '$locationProvider'];
    function config($routeProvider, $locationProvider) {
        $routeProvider
            .when('/chat/:cid/:uid', {
                controller: 'ChatController',
                templateUrl: 'pages/chat.html',
                controllerAs: 'vm'
            })

            .when('/login', {
                controller: 'LoginController',
                templateUrl: 'pages/login.html',
                controllerAs: 'vm'
            })

            .when('/register', {
                controller: 'RegisterController',
                templateUrl: 'pages/register.html',
                controllerAs: 'vm'
            })

	        .when('/main/:uid', {
                controller: 'MainPageController',
                templateUrl: 'pages/mainpage.html',
                controllerAs: 'vm'
            })
        
            .when('/addChat/:uid', {
                controller: 'AddChatController',
                templateUrl: 'pages/addChat.html',
                controllerAs: 'vm'
            })
        
            .when('/addContact/:uid', {
                controller: 'AddContactController',
                templateUrl: 'pages/addContact.html',
                controllerAs: 'vm'
            })

            .when('/addParticipant/:cid/:uid', {
                controller: 'AddParticipantController',
                templateUrl: 'pages/addParticipant.html',
                controllerAs: 'vm'
            })
            
            .when('/reply/:uid/:cid/:mid', { ///reply/:disp/:uid/:gid/:mid
                controller: 'ReplyController',
                templateUrl: 'pages/reply.html',
                controllerAs: 'vm'
            })    
         
            .when('/removeContact/:uid', {
                controller: 'removeContactController',
                templateUrl: 'pages/removeContact.html',
                controllerAs: 'vm'
            })    
        
            .when('/removeParticipant/:cid/:uid', {
                controller: 'removeParticipantController',
                templateUrl: 'pages/removeParticipant.html',
                controllerAs: 'vm'
            })

            .when('/likes/:pid', {
                controller: 'LikesController',
                templateUrl: 'pages/like.html',
                controllerAs: 'vm'
            })

            .when('/dislikes/:pid', {
                controller: 'DislikesController',
                templateUrl: 'pages/dislike.html',
                controllerAs: 'vm'
            })

            .when('/removeChat/:uid', {
                controller: 'removeChatController',
                templateUrl: 'pages/removeChat.html',
                controllerAs: 'vm'
            })

            .when('/dashboard/:uid', {
                controller: 'DashboardController',
                templateUrl: 'pages/dashboard.html',
                controllerAs: 'vm'
            })

            .otherwise({ redirectTo: '/login' });
    }

    run.$inject = ['$rootScope', '$location', '$cookies', '$http'];
    function run($rootScope, $location, $cookies, $http) {
        // keep user logged in after page refresh
        $rootScope.globals = $cookies.getObject('globals') || {};
        if ($rootScope.globals.currentUser) {
            $http.defaults.headers.common['Authorization'] = 'Basic ' + $rootScope.globals.currentUser.authdata;
        }

        $rootScope.$on('$locationChangeStart', function (event, next, current) {
            // redirect to login page if not logged in and trying to access a restricted page
            var restrictedPage = $.inArray($location.path(), ['/main/:uid','/chat/:cid/:uid', '/login', '/register',
                '/addContact','/addChat/:uid','/reply:uid/:cid/:mid', 'addParticipant/:cid/:uid', '/likes/:pid', '/removeChat/:uid',
            '/dashboard/:uid']) === -1;
            var loggedIn = $rootScope.globals.currentUser;
            if (restrictedPage && !loggedIn) {
                $location.path('/login');
            }
        });
    }

})();
