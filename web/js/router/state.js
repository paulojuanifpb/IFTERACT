app.config(function ($stateProvider, $urlRouterProvider) {

    // Rota padrão.
    $urlRouterProvider.otherwise("/");

    // Estados
    $stateProvider
        .state("login", {
            url:"/",
            controller: "loginCtrl",
            templateUrl: "login.html"
        })
});