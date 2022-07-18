function filtrarDatos() {
    let filas = document.getElementsByTagName('td');
    let fechaDesde = document.getElementById('fechaDesde').value;
    let fechaHasta = document.getElementById('fechasHasta').value;
    let areas = document.getElementById('selectArea');
    let areaSelecet = areas.options[areas.selectedIndex].text;
    let regex = /^[0-9]*$/;
    let fechaFormat = Date.parse(fechaDesde);

    let fecha = new Date(fechaFormat);
    console.log(fecha)
    for (x in filas){
        if( regex.test(x)){

        }
        else{
            //pass
        }
    }
}