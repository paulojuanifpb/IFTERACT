app.factory("usuarioService", function($http){


    var _path = "http://127.0.0.1:5000";

    var _cadastrar = function(user){
        $http.post(_path + "/cadastrar", user)
    }

    var _logar = function(perfil){

        var dados;
        $http.post(_path + "/logar", perfil).then(function(response){
            dados = response.data;
        })
        return dados;
    }

    var _home = function(){
        $http.get(_path + "/home")

    }

    var _buscarPerfil = function(){
        $http.get(_path + "/inf")
    }

    return{
        cadastrar: _cadastrar,
        logar: _logar,
        home: _home,
        buscarPerfil: _buscarPerfil
    };

});
