let regexString =/^[a-zA-ZÀ-ÿ\s]{1,40}$/;

function validarForm() {
    let selectForm = document.getElementById('state_id');
    let select_idEspec = selectForm.options[selectForm.selectedIndex].text;
    let descripcion = document.getElementById('descripcion').value;



    document.formulario.submit();
}

function blanquearSelect() {
    document.getElementById('error_form_select').style.display = "None";
}
function blanquearDescripcion() {
    document.getElementById('error_form_descripcion').style.display = "None";
}