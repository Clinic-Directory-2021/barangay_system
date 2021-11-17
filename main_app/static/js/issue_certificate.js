

function indigentModal(first_name, middle_name, last_name, age , resident_id){
    $('#indigent_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#indigent_age').val(age);
    $('#indigent_resident_id').val(resident_id);
}

function clearanceModal(first_name, middle_name, last_name, age , resident_id){
    $('#clearance_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#clearance_age').val(age);
    $('#clearance_resident_id').val(resident_id);
}

function buildingModal(first_name, middle_name, last_name, age , resident_id){
    $('#building_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#building_age').val(age);
    $('#building_resident_id').val(resident_id);
}

function residencyModal(first_name, middle_name, last_name, age , resident_id, birthdate, civil_status , birthplace){
    $('#residency_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#residency_age').val(age);
    $('#residency_resident_id').val(resident_id);
    $('#residency_birthdate').val(birthdate);
    $('#residency_civil_status').val(civil_status);
    $('#residency_birthplace').val(birthplace);
}

function wiringModal(first_name, middle_name, last_name, resident_id){
    $('#wiring_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#wiring_resident_id').val(resident_id);
}

function excavationModal(first_name, middle_name, last_name, resident_id){
    $('#excavation_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#excavation_resident_id').val(resident_id);
}

function fencingModal(first_name, middle_name, last_name, resident_id){
    $('#fencing_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#fencing_resident_id').val(resident_id);
}

function waterModal(first_name, middle_name, last_name, resident_id){
    $('#water_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#water_resident_id').val(resident_id);
}

function blotterModal(first_name, middle_name, last_name, resident_id){
    $('#blotter_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#blotter_resident_id').val(resident_id);
}