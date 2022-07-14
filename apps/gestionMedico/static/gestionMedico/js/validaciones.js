var regexString =  /^[a-zA-ZÀ-ÿ\s]{1,40}$/;
var regexRut = /^[0-9]+[-|‐]{1}[0-9]{1}$/

function validaForm() {
    var rut_especialista = document.getElementById('rut_espc').value;
    var nombre_espc = document.getElementById('nombre_espc').value;
    var apellido_espc = document.getElementById('apellido_espc').value;
    var id_especialidad = document.getElementById('id_especialidad');
    var select_idEspec = id_especialidad.options[id_especialidad.selectedIndex].text;
    var rutSeparado = rut_especialista.split('-',2)
    var rutPrimeraParte = rutSeparado[0]
    var rutSegundaParte = rutSeparado[1]

    if((rut_especialista.length === 0) ||(nombre_espc.length === 0) || (apellido_espc.length === 0) || (select_idEspec.length === 0) ){
        document.getElementById('error_form_rut').style.display="block";
        document.getElementById('error_form_rut').innerHTML = 'Debe rellenar todos los campos';
        return 0;
    }
    if (!regexRut.test(rut_especialista)){

        document.getElementById('error_form_rut').style.display="block";
        document.getElementById('error_form_rut').innerHTML = 'Debe ingresar un rut valido (ej:xxxxxxxxx-x)';
        return 0; 

    }
    if(rutSegundaParte.length > rutPrimeraParte.length){
        document.getElementById('error_form_rut').style.display="block";
        document.getElementById('error_form_rut').innerHTML = 'Demaciado caracteres para un rut valido, vuelva a ingresar (ej:xxxxxxxxx-x)';
        return 0; 
    }
    if(rut_especialista.length < 9 && rut_especialista.length > 11){
        document.getElementById('error_form_rut').style.display="block";
        document.getElementById('error_form_rut').innerHTML = 'Ingreso un rut invalido, ingrese un nuevo rut';
        return 0;
    }
    if(nombre_espc.length > 25) {
        document.getElementById('error_form_nombre').style.display="block";
        document.getElementById('error_form_nombre').innerHTML = 'EL nombre ingresado contiene demaciados caracteres, debe ingresar uno menor';
        return 0;

    }
    if(regexString.test(nombre_espc)){
        //pass
    }else{
        document.getElementById('error_form_nombre').style.display="block";
        document.getElementById('error_form_nombre').innerHTML = 'El nombre ingresado lleva carcateres no aceptados';
        return 0;
    }
    if(regexString.test(apellido_espc)){
        //pass
    }else{
        document.getElementById('error_form_apellido').style.display="block";
        document.getElementById('error_form_apellido').innerHTML = 'El apellido ingresado lleva carcateres no aceptados';
        return 0;
    }
    if(apellido_espc.length < 2){
        document.getElementById('error_form_correo').style.display="block";
        document.getElementById('error_form_correo').innerHTML = 'Debe ingresar un correo de tamaño mayor a 12 caracteres';
        return 0;
    }
    if(select_idEspec === "---------"){
        document.getElementById('error_form_especialidad').style.display="block";
        document.getElementById('error_form_especialidad').innerHTML = 'Debe seleccionar una especialidad';
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
function blanquearApellido() {
    document.getElementById('error_form_apellido').style.display = "None";
}
function blanquearEspec() {
    document.getElementById('error_form_especialidad').style.display = "None";
}