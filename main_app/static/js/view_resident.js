
function viewResident(resident_id){

    var url = "/resident_profile";

    // Construct the full URL with "id"
    document.location.href = url + "?resident_id=" + resident_id;
    
}