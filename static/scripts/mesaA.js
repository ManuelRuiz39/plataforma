function selecciona() {

    var opt = $('#niveles').val();

    if (opt == "default") {
        $('#n1').hide();
        $('#n2').hide();
        $('#n3').hide();
    }
    if (opt == "nivel1"){
        $('#n1').show();
        $('#n2').hide();
        $('#n3').hide();
    }
    if (opt == "nivel2") {
        $('#n1').hide();
        $('#n2').show();
        $('#n3').hide();
    }
    if (opt == "nivel3") {
        $('#n1').hide();
        $('#n2').hide();
        $('#n3').show();
    }
}
