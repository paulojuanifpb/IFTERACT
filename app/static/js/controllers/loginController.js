app.controller("loginController", function($scope, usuarioService){

    $scope.usuario;

    var cadastrar = function(){

        var user = $scope.usuario;

        usuarioService.cadastrar(user)
        console.log("Deu certo")


    };


});