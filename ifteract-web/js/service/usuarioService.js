app.factory("usuarioService", function($http, config){


    var _path = config.baseUrl() + "";

    var _cadastrar = function(user){
        $http.post(_path + "cadastrar", user)
    }

    var _logar = function(perfil){
        
        $http.post(_path + "logar", perfil)
            
    }

    return{
        cadastrar: _cadastrar,
        logar: _logar
    };

});