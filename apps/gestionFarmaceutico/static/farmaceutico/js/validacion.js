let regexString =/^[a-zA-ZÀ-ÿ\s]{1,40}$/;

function validarForm() {
    let selectForm = document.getElementById('state_id');
    let select_idEspec = selectForm.options[selectForm.selectedIndex].text;
    let descripcion = document.getElementById('descripcion').value;

    if((select_idEspec == "------") ){
        document.getElementById('error_form_select').style.display="block";
        document.getElementById('error_form_select').innerHTML = 'Debe rellenar el campo estado.';
        return 0;
    }
    if(descripcion.length > 0){
        if(regexString.test(descripcion)){
            //pass
        }else{
            document.getElementById('error_form_descripcion').style.display="block";
            document.getElementById('error_form_descripcion').innerHTML = 'La descripcion ingresado lleva carcateres no aceptados';
            return 0;
        }
    }

    document.formulario.submit();
}

function blanquearSelect() {
    document.getElementById('error_form_select').style.display = "None";
}
function blanquearDescripcion() {
    document.getElementById('error_form_descripcion').style.display = "None";
}