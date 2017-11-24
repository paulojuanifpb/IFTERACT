app.config(function ($stateProvider, $urlRouterProvider) {

    // Rota padrão.

    // Estados
    $stateProvider
        .state("home", {
            url:"/home",
            controller: "homeCtrl",
            templateUrl: "view/home.html"
        })
});