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

    $scope.logar = function(perfil){

        console.log(perfil);


        usuarioService.logar(perfil);
        $state.go("home")


    };

});
