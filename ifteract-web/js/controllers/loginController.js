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
        
        var requisicao = usuarioService.logar(perfil);
        requisicao.then(function(response){

            console.log("cheguei");
            var dados = response.data;
            console.log(dados);
        });
        
        return requisicao;
        //$state.transitionTo("home");
        //location.reload();

    };

});
