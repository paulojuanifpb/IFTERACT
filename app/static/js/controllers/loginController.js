app.controller('loginCtrl', function($scope, usuarioService){

    $scope.usuario;
    console.log("CHEGOUUU");

    $scope.oi ="oi";
    $scope.cadastrar = function(){

        var user = $scope.usuario;

        usuarioService.cadastrar(user)
        console.log("Deu certo")


    };


});
