$( document ).ready(function() {
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