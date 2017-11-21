app.config(function ($stateProvider, $urlRouterProvider, $locationProvider) {

    // Rota padrão.
    $urlRouterProvider.otherwise("/");

    $locationProvider.hashPrefix('');
    $locationProvider.html5Mode({
    enabled:true,
    requireBase: false

    })
    // Estados
    $stateProvider
        .state("home", {
            url:"/home",
            controller: "homeCtrl",
        })
});