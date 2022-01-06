/* jshint esversion: 8, jquery: true */
let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#800080');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#800080');
    } else {
        $(this).css('color', '#008000');
    }
});