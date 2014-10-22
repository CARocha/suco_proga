function show_solo_jovenes_con_dos (numero_encuesta)
{
    if (numero_encuesta == 3) {
        $('#solo_jovenes_con_dos_wrapper').show();
    } else {
        $('#solo_jovenes_con_dos_wrapper').hide();
    }
}



$( document ).ready(function() {

    show_solo_jovenes_con_dos ($("#id_numero_encuesta").val())

    //Encuesta comparar(3): necesitamos saber si utilisamos solo jovenes que tienen 2 encuestas
    $("#id_numero_encuesta").change(function () {
        show_solo_jovenes_con_dos($(this).val())
    });

    $('.format_diff').each(function() {
        var val = $(this).html();

        if (val[val.length -1] == "%") {
            val = val.replace('%', '');
        }

        if (val > 0) {
            $(this).addClass('green_cell');
        } else if (val < 0) {
            $(this).addClass('red_cell');
        }
    });
});