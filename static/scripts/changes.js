function selecciona() {

    var opt = $('#opc').val();
    var opt1 = $('#hard').val();
    var opt2 = $('#serv').val();
    var opt3 = $('#servS').val();
    var opt4 = $('#redes').val();
    var opt5 = $('#monitoreo').val();
    var opt6 = $('#monitor').val();

    if (opt == "cat") {
        $('#servicios').hide();
        $('#hardware').hide();
        $('#software').hide();
    }
    if (opt == "hardware") {
        $('#hardware').show();
        $('#software').hide();
        $('#monitoreo').hide();
        if (opt1 == "servidores") {
            $('#software').hide();
            $('#servicios').show();
            $('#serviciosS').hide();
            $('#red').hide();
            if (opt2 == "instalacionF") {
                $('#software').hide();
                $('#startup').hide();
                $('#sistema').hide();
                $('#basico').show();
                $('#fisicaS').hide();
                $('#startupStor').hide();
                $('#switch').hide();
                $('#wireless').hide();
            }
            if (opt2 == "startup") {
                $('#software').hide();
                $('#startup').show();
                $('#sistema').hide();
                $('#basico').hide();
                $('#fisicaS').hide();
                $('#startupStor').hide();
                $('#switch').hide();
                $('#wireless').hide();
            }
            if (opt2 == "instalacionO") {
                $('#software').hide();
                $('#startup').hide();
                $('#sistema').show();
                $('#basico').hide();
                $('#fisicaS').hide();
                $('#startupStor').hide();
                $('#switch').hide();
                $('#wireless').hide();
            }

        }
        if (opt1 == "almacenamiento") {
            $('#software').hide();
            $('#servicios').hide();
            $('#red').hide();
            $('#serviciosS').show();
            if (opt3 == "instalacionS") {
                $('#software').hide();
                $('#startup').hide();
                $('#sistema').hide();
                $('#basico').hide();
                $('#fisicaS').show();
                $('#startupStor').hide();
                $('#switch').hide();
                $('#wireless').hide();
            }
            if (opt3 == "startupStorage") {
                $('#software').hide();
                $('#startup').hide();
                $('#sistema').hide();
                $('#basico').hide();
                $('#fisicaS').hide();
                $('#startupStor').show();
                $('#switch').hide();
                $('#wireless').hide();
            }
        }

        if (opt1 == "redes") {
            $('#software').hide();
            $('#servicios').hide();
            $('#serviciosS').hide();
            $('#red').show();
            if (opt4 == "swi") {
                $('#software').hide();
                $('#startup').hide();
                $('#sistema').hide();
                $('#basico').hide();
                $('#fisicaS').hide();
                $('#startupStor').hide();
                $('#switch').show();
                $('#wireless').hide();
            }
            if (opt4 == "wifi") {
                $('#software').hide();
                $('#startup').hide();
                $('#sistema').hide();
                $('#basico').hide();
                $('#fisicaS').hide();
                $('#startupStor').hide();
                $('#switch').hide();
                $('#wireless').show();
            }
        }
    } else {
        $('#hardware').hide();
        $('#software').show();
        $('#servicios').hide();
        $('#monitoreo').hide();
    }
    if (opt == "monitoreo"){
        $('#hardware').hide();
        $('#software').hide();
        $('#servicios').hide();
        $('#monitoreo').show();
        if(opt6 == "monitor"){
            $('#mw').show();
            $('#').show();
        }
    }
}
