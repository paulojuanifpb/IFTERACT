app.controller('loginCtrl', function($scope, $state, usuarioService){

    $scope.usuario;
    $scope.perfil;

    console.log("CHEGOUUU");

    $scope.oi ="oi";
    $scope.cadastrar = function(){

        var user = $scope.usuario;

        usuarioService.cadastrar(user);
        console.log("Deu certo");


    };

    $scope.logar = function(){

        console.log("Logou");

        var perfil = $scope.perfil;


        usuarioService.logar(perfil);
        console.log(usuarioService.home());
        $state.transitionTo("home", {reload: true});
        location.reload();

    };

});
