

function indigentModal(first_name, middle_name, last_name, age , resident_id, request_id, purpose, email){
    $('#indigent_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#indigent_age').val(age);
    $('#indigent_resident_id').val(resident_id);
    $('#indigent_request_id').val(request_id);
    $('#indigent_purpose').val(purpose);
    
    $('#email_field_indigent').val(email);
}

function clearanceModal(first_name, middle_name, last_name, age , resident_id, request_id, email){
    $('#clearance_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#clearance_age').val(age);
    $('#clearance_resident_id').val(resident_id);
    $('#clearance_request_id').val(request_id);

    $('#email_field_clearance').val(email);
}

function buildingModal(first_name, middle_name, last_name, age , resident_id, request_id, email){
    $('#building_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#building_age').val(age);
    $('#building_resident_id').val(resident_id);
    $('#building_request_id').val(request_id);

    $('#email_field_building').val(email);
}

function residencyModal(first_name, middle_name, last_name, age , resident_id, birthdate, civil_status , birthplace, request_id, email){
    $('#residency_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#residency_age').val(age);
    $('#residency_resident_id').val(resident_id);
    $('#residency_birthdate').val(birthdate);
    $('#residency_civil_status').val(civil_status);
    $('#residency_birthplace').val(birthplace);
    $('#residency_request_id').val(request_id);

    $('#email_field_residency').val(email);
}

function wiringModal(first_name, middle_name, last_name, resident_id, request_id, email){
    $('#wiring_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#wiring_resident_id').val(resident_id);
    $('#wiring_request_id').val(request_id);

    $('#email_field_wiring').val(email);
}

function excavationModal(first_name, middle_name, last_name, resident_id, request_id, email){
    $('#excavation_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#excavation_resident_id').val(resident_id);
    $('#excavation_request_id').val(request_id);
    $('#email_field_excavation').val(email);
}

function fencingModal(first_name, middle_name, last_name, resident_id, request_id, email){
    $('#fencing_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#fencing_resident_id').val(resident_id);
    $('#fencing_request_id').val(request_id);

    $('#email_field_fencing').val(email);
}

function waterModal(first_name, middle_name, last_name, resident_id, request_id, email){
    $('#water_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#water_resident_id').val(resident_id);
    $('#water_request_id').val(request_id);

    $('#email_field_water').val(email);
}

function blotterModal(first_name, middle_name, last_name, resident_id, request_id, email, complaint){
    $('#blotter_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#blotter_resident_id').val(resident_id);
    $('#blotter_request_id').val(request_id);

    $('#email_field_blotter').val(email);

    $('#complaint').val(complaint);

    $('#complaintText').text(complaint)
}

function businessModal(first_name, middle_name, last_name, resident_id, request_id, email,place_of_business,applicant_name, certificate_type){
    $('#business_full_name').val(first_name.toUpperCase()  + ' ' + middle_name.toUpperCase()  + ' ' + last_name.toUpperCase());
    $('#business_resident_id').val(resident_id);
    $('#business_request_id').val(request_id);

    $('#email_field_business').val(email);

    $('#place_of_business').val(place_of_business);
    $('#applicant_name').val(applicant_name);

    $('#certificate_type').val(certificate_type);
    
}