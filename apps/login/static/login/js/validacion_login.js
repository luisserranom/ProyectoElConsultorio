document.addEventListener("DOMContentLoaded", function() {
    var label_error = document.getElementById('label_error');
    label_error.setAttribute("atribute","disabled")

});

function validaForm() {
    var usuario = document.getElementById('usuario').value;
    var password = document.getElementById('password').value;
    var expresionRut = "/^[0-9]+[-|‐]{1}[0-9kK]{1}$/"
    if(usuario.length < 8){
        document.getElementById('label_error').removeAttribute("disabled");
        document.getElementById('label_error').innerHTML = 'EL USUARIO DEBE SER UN RUT IGUAL O MAYOR A 9';
        document.formulario.usuario.focus()
        return 0;
    }
    document.formulario.submit();
}