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

        console.log("TESTANDO SO CAMAANDO A FUNCAO");
        usuarioService.logar(perfil);

        console.log("TESTANDO SO CAMAANDO A FUNCAO COM CONSOLE");
        console.log(usuarioService.logar(perfil));

        console.log("TESTANDO SO CAMAANDO A COM CONSOLE BUSCAR");
        console.log(usuarioService.buscarPerfil());

        var user = usuarioService.buscarPerfil();
        console.log("TESTANDO SO CAMAANDO A VARIAVEL")
        console.log(user);
        $state.transitionTo("home", {reload: true});
        //location.reload();

    };

});
