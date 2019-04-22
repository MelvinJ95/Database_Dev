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

        .when('/addParticipant/:uid', {
                controller: 'AddParticipantController',
                templateUrl: 'pages/addParticipant.html',
                controllerAs: 'vm'
            })
            
        .when('/reply', { ///reply/:disp/:uid/:gid/:mid
                controller: 'ReplyController',
                templateUrl: 'pages/reply.html',
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
            var restrictedPage = $.inArray($location.path(), ['/main/:uid','/chat/:cid/:uid', '/login', '/register','/addContact','/addChat/:uid','/reply']) === -1;
            var loggedIn = $rootScope.globals.currentUser;
            if (restrictedPage && !loggedIn) {
                $location.path('/login');
            }
        });
    }

})();
