
function viewResident(resident_id){

    var url = "../resident_profile";

    // Construct the full URL with "id"
    document.location.href = url + "?resident_id=" + resident_id;
    
}
function editResident(resident_id, old_img_file_directory, email){
    window.location.href = "../edit_resident/?resident_id="+resident_id+ "&old_img_file_directory=" +old_img_file_directory + "&email=" + email;
}

function restoreResident(resident_id){
    var url = "../restore_resident";

    // Construct the full URL with "id"
    document.location.href = url + "?resident_id=" + resident_id;
}