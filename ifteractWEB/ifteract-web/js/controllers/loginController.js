app.controller('loginCtrl', function($scope, $state, usuarioService){

    $scope.usuario;
    $scope.perfil;
    $scope.mostrarFormulario = false;

    console.log("CHEGOUUU");

    $scope.oi ="oi";
    $scope.cadastrar = function(){

        var user = $scope.usuario;
        if(!user.publico){
            user.publico = false;
        }
        usuarioService.cadastrar(user);
        console.log("Deu certo");
        console.log(user);


    };

    $scope.logar = function(perfil){

        var perfil = $scope.perfil;
        console.log(perfil);
        
        var requisicao = usuarioService.logar(perfil);
        requisicao.then(function(response){

            console.log("cheguei");
            var dados = response.data;
            console.log(dados);
            $state.go("home");
        });
        
        return requisicao;
        $state.go("home");
        

    };

    $scope.mostrarCadastro = function(){
        console.log("CHEGOU NO MOSTRAR");
        $scope.mostrarFormulario = !$scope.mostrarFormulario;
    }
});
