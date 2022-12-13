function identity_check() {
    var id_value = $(this).prop('id');
    var title_value = $('#'+id_value).attr('title');
    window.alert(title_value);
}