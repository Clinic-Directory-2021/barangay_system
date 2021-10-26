

function indigentModal(first_name, middle_name, last_name, age , resident_id){
    $('#indigent_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#indigent_age').val(age);
    $('#indigent_resident_id').val(resident_id);
}