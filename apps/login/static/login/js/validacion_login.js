/*document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formulario").addEventListener('submit', validarFormulario); 
    var label_error = document.getElementById('label_error');
    label_error.setAttribute("atribute","disabled")
  });
  function validarFormulario(e) {
    e.preventDefault
    var usuario = document.getElementById('usuario').value;
    var password = document.getElementById('password').value;
    if(usuario.length < 8){
        alert("error")
        document.getElementById('label_error').removeAttribute("disabled");
        document.getElementById('label_error').innerHTML = 'EL USUARIO DEBE SER UN RUT IGUAL O MAYOR A 9';
        return 0;
    }
  }*/

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