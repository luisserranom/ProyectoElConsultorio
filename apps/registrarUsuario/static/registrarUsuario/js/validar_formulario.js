document.addEventListener("DOMContentLoaded", function() {
    var label_error = document.getElementById('error_form_rut');
    label_error.setAttribute("atribute","hidden")
    var label_error = document.getElementById('error_form_nombre');
    label_error.setAttribute("atribute","hidden")

});

function validaForm() {
    var nombre = document.getElementById('nombre').value;
    var Papellido = document.getElementById('Papellido').value;
    var Sapellido = document.getElementById('Sapellido').value;
    var rut = document.getElementById('rut').value;
    var correo = document.getElementById('correo').value;
    var psw1 = document.getElementById('psw1').value;
    var psw2 =document.getElementById('psw2').value;
    var rutSeparado = rut.split('-',2)
    var rutPrimeraParte = rutSeparado[0]
    var rutSegundaParte = rutSeparado[1]
    console.log(rutPrimeraParte)
    console.log(rutSegundaParte)

    if((nombre.length === 0) ||(Papellido.length === 0) || (Sapellido.length === 0) || (rut.length === 0) || (correo.length === 0) || (psw1.length === 0) || 
    (psw2.length === 0)  ){
        document.getElementById('error_form_rut').style.display="block";
        document.getElementById('error_form_rut').innerHTML = 'Debe rellenar todos los campos';
        return 0;
}
    if (!/^[0-9]+[-|‐]{1}[0-9]{1}$/.test( rut )){
        document.getElementById('error_form_rut').style.display="block";
        document.getElementById('error_form_rut').innerHTML = 'Debe ingresar un rut valido a (ej:xxxxxxxxx-x)';
        document.getElementById('rut').focus();
        return 0; 
    }
    if(rutSegundaParte.length > rutPrimeraParte.length){
        document.getElementById('error_form_rut').style.display="block";
        document.getElementById('error_form_rut').innerHTML = 'Debe ingresar un rut valido b(ej:xxxxxxxxx-x)';
        document.getElementById('rut').focus();
        return 0; 
    }
    if(rut.length < 9 && rut.length > 11){
        document.getElementById('error_form_rut').style.display="block";
        document.getElementById('error_form_rut').innerHTML = 'Ingreso un rut invalido, ingrese un nuevo rut';
        document.getElementById('rut').focus();
        return 0;
    }
    if(nombre.length > 25) {
        document.getElementById('error_form_nombre').style.display="block";
        document.getElementById('error_form_nombre').innerHTML = 'EL nombre ingresado contiene demaciados caracteres, debe ingresar uno menor';
        document.getElementById('rut').focus();
        return 0;

    }
    if( /^[a-zA-ZÀ-ÿ\s]{1,40}$/.test(nombre)){
        //pass
    }else{
        document.getElementById('error_form_nombre').style.display="block";
        document.getElementById('error_form_nombre').innerHTML = 'El nombre ingresado lleva carcateres no aceptados';
        document.getElementById('rut').focus();
        return 0;
    }
    if(psw1.length < 8){
        document.getElementById('error_form_psw1').style.display="block";
        document.getElementById('error_form_psw1').innerHTML = 'Debe ingresar una contraseña de tamaño mayor a 8';
        document.getElementById('psw1').focus();
        return 0;
    }
    if(psw2.length < 8){
        document.getElementById('error_form_psw2').style.display="block";
        document.getElementById('error_form_psw2').innerHTML = 'Debe ingresar una contraseña de tamaño mayor a 8';
        document.getElementById('psw2').focus();
        return 0;
    }
    if(psw1 != psw2 ){
        document.getElementById('error_form_psw2').style.display="block";
        document.getElementById('error_form_psw2').innerHTML = 'Debe rellenar todos los campos';
        document.getElementById('psw2').focus();
        return 0;
    }
    document.formulario.submit();
}

function blanquearRut() {
    document.getElementById('error_form_rut').style.display = "None";
}
function blanquearNombre() {
    document.getElementById('error_form_nombre').style.display = "None";
}
function blanquearPapellido() {
    document.getElementById('error_form_Papellido').style.display = "None";
}
function blanquearSapellido() {
    document.getElementById('error_form_Sapellido').style.display = "None";
}
function blanquearCorreo() {
    document.getElementById('error_form_Correo').style.display = "None";
}
function blanquearPsw1() {
    document.getElementById('error_form_psw1').style.display = "None";
}
function blanquearPsw2() {
    document.getElementById('error_form_psw2').style.display = "None";
}
