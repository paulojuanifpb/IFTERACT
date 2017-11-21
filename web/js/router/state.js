app.config(function ($stateProvider, $urlRouterProvider) {

    // Rota padrão.
    $urlRouterProvider.otherwise("/");

    // Estados
    $stateProvider
        .state("home", {
            url:"/home",
            controller: "homeCtrl",
            templateUrl: "home.html"
        })
});