app.config(function ($stateProvider, $urlRouterProvider) {

    // Rota padrão.
    
    $urlRouterProvider.otherwise('/login');

    // Estados
    $stateProvider
        .state("home", {
            url:"/home",
            controller: "homeCtrl",
            templateUrl: "view/home.html",
        })
        .state("login",{
            url:"/login",
            controller: "loginCtrl",
            templateUrl: "view/login.html",
            
    })
});