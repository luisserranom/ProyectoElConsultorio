let regexString =  /^[a-zA-ZÀ-ÿ\s]{1,40}$/;
let regexCorreo = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/
let regexRut = /^[0-9]+[-|‐]{1}[0-9]{1}$/
let regexPassword =/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){8,15}$/;


document.addEventListener("DOMContentLoaded", function() {
    var label_error = document.getElementById('error_form_rut');
    label_error.setAttribute("atribute","hidden")
    var label_error = document.getElementById('error_form_nombre');
    label_error.setAttribute("atribute","hidden")

});

function validaForm() {
    let nombre = document.getElementById('nombre').value;
    let Papellido = document.getElementById('Papellido').value;
    let Sapellido = document.getElementById('Sapellido').value;
    let rut = document.getElementById('rut').value;
    let correo = document.getElementById('correo').value;
    let psw1 = document.getElementById('psw1').value;
    let psw2 =document.getElementById('psw2').value;
    let rutSeparado = rut.split('-',2)
    let rutPrimeraParte = rutSeparado[0]
    let rutSegundaParte = rutSeparado[1]

    if((nombre.length === 0) ||(Papellido.length === 0) || (Sapellido.length === 0) || (rut.length === 0) || (correo.length === 0) || (psw1.length === 0) || 
    (psw2.length === 0)  ){
        document.getElementById('error_form_rut').style.display="block";
        document.getElementById('error_form_rut').innerHTML = 'Debe rellenar todos los campos';
        return 0;
    }
    if (!regexRut.test(rut)){

        document.getElementById('error_form_rut').style.display="block";
        document.getElementById('error_form_rut').innerHTML = 'Debe ingresar un rut valido (ej:xxxxxxxxx-x)';
       
        return 0; 

    }
    if(rutSegundaParte.length > rutPrimeraParte.length){
        document.getElementById('error_form_rut').style.display="block";
        document.getElementById('error_form_rut').innerHTML = 'Demaciado caracteres para un rut valido, vuelva a ingresar (ej:xxxxxxxxx-x)';
       
        return 0; 
    }
    if(rut.length < 9 && rut.length > 11){
        document.getElementById('error_form_rut').style.display="block";
        document.getElementById('error_form_rut').innerHTML = 'Ingreso un rut invalido, ingrese un nuevo rut';
        return 0;
    }
    if(nombre.length > 25) {
        document.getElementById('error_form_nombre').style.display="block";
        document.getElementById('error_form_nombre').innerHTML = 'EL nombre ingresado contiene demaciados caracteres, debe ingresar uno menor';
        return 0;

    }
    if(regexString.test(nombre)){
        //pass
    }else{
        document.getElementById('error_form_nombre').style.display="block";
        document.getElementById('error_form_nombre').innerHTML = 'El nombre ingresado lleva carcateres no aceptados';
        return 0;
    }
    if(Papellido.length > 25) {
        document.getElementById('error_form_Papellido').style.display="block";
        document.getElementById('error_form_Papellido').innerHTML = 'EL apellido ingresado contiene demaciados caracteres, debe ingresar uno menor';
        return 0;
    }
    if(regexString.test(Papellido)){
        //pass
    }else{
        document.getElementById('error_form_Papellido').style.display="block";
        document.getElementById('error_form_Papellido').innerHTML = 'El apellido ingresado lleva carcateres no aceptados';
        return 0;
    }

    if(Sapellido.length > 25) {
        document.getElementById('error_form_Sapellido').style.display="block";
        document.getElementById('error_form_Sapellido').innerHTML = 'EL apellido ingresado contiene demaciados caracteres, debe ingresar uno menor';
        return 0;

    }
    if(regexString.test(Sapellido)){
        //pass
    }else{
        document.getElementById('error_form_Sapellido').style.display="block";
        document.getElementById('error_form_Sapellido').innerHTML = 'El apellido ingresado lleva carcateres no aceptados';
        return 0;
    }
    if(correo.length < 12){
        document.getElementById('error_form_correo').style.display="block";
        document.getElementById('error_form_correo').innerHTML = 'Debe ingresar un correo de tamaño mayor a 12 caracteres';
        return 0;
    }
    if(regexCorreo.test(correo)){
        //pass
    }else{
        document.getElementById('error_form_correo').style.display="block";
        document.getElementById('error_form_correo').innerHTML = 'El correo ingresado no es invalid (ej:xxxx@xxx.xx)';
        return 0;
    }
    if(psw1.length < 8){
        document.getElementById('error_form_psw1').style.display="block";
        document.getElementById('error_form_psw1').innerHTML = 'Debe ingresar una contraseña de tamaño mayor a 8';
        return 0;
    }
    if(regexPassword.test(psw1)){
        //pass
    }else{
        document.getElementById('error_form_psw1').style.display="block";
        document.getElementById('error_form_psw1').innerHTML = 'La contraseña debe tener:\t-minimo 8 caracteres\t-minimo 1 caracter mayuscula\t-minimo 1 punto\t-al menos 1 caracter especial(!#$%&)';
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
        document.getElementById('error_form_psw2').innerHTML = 'Las contraseña no son iguales';
        document.getElementById('psw2').focus();
        return 0;
    }
    document.formulario.submit();
}


//FUNCIONES PARA BLANQUEAR 

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
    document.getElementById('error_form_correo').style.display = "None";
}
function blanquearPsw1() {
    document.getElementById('error_form_psw1').style.display = "None";
}
function blanquearPsw2() {
    document.getElementById('error_form_psw2').style.display = "None";
}
