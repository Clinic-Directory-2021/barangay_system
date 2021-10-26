

function deleteResident(resident_id, img_directory){

        Swal.fire({
            icon: 'question',
            title: 'Do you Really Want to Delete this Resident?',
            text: 'This Cannot Be Undone!',
            showDenyButton: true,
            showCancelButton: true,
            showConfirmButton: false,
            denyButtonText: `Delete`,
          }).then((result) => {
              if (result.isDenied) {
                var url = "/delete_resident";

                // Construct the full URL with "id"
                document.location.href = url + "?resident_id=" + resident_id + "&img_directory="+ img_directory;
            }
          })
    
}