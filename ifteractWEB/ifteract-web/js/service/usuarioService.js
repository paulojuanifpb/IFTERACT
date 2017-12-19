app.factory("usuarioService", function($http, config){


    var _path = config.baseUrl() + "";

    var _cadastrar = function(user){
        return $http.post(_path + "cadastrar", user)
    }

    var _logar = function(perfil){
        
        return $http.post(_path + "logar", perfil)
            
    }

    return{
        cadastrar: _cadastrar,
        logar: _logar
    };

});