app.factory("usuarioService", function($http){


    var _path = "http://127.0.0.1:5000";

    var _cadastrar = function(user){
        $http.post(_path + "/cadastrar", user)
    }

    return{
        cadastrar: _cadastrar
    };

});