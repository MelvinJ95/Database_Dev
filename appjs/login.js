(function () {
    'use strict';

    angular
        .module('AppChat')
        .controller('LoginController', LoginController);

    LoginController.$inject = ['$http','$location', 'AuthenticationService', 'FlashService', 'UserService'];
    function LoginController($http, $location, AuthenticationService, FlashService, UserService) {
        var UserInfo;
        var vm = this;
        var UserID=0; 
        var JsonP; 
        vm.login = login;

        (function initController() {
            // reset login status
            AuthenticationService.ClearCredentials();
        })();

        function login() {
            vm.dataLoading = true;
            AuthenticationService.Login(vm.username, vm.password, function (response) {
                if (response.success) {
                    AuthenticationService.SetCredentials(vm.username, vm.password);
                    $http.get('http://localhost:5000/GramChat/users/info/' + vm.username).then(function (response){
                    console.log("response: " + JSON.stringify(response));
            
                    UserInfo = response.data.User;
                    console.log(UserInfo.uid);
                    UserID = UserInfo.uid;
                    $location.path('/main/'+UserID);
        
        }, handleError('Error getting user by username'));
                } else {
                    
                    FlashService.Error(response.message);
                    vm.dataLoading = false;
                }
            });
        };
    }
    function handleError(error) {
        return function () {
            return { success: false, message: error };
        };
    }
})();
