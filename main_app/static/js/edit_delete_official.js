
function editOfficial(official_id, full_name, position, term_duration, status, purok, official_img_directory){
   
    $('#official_id_edit').val(official_id);
    $('#full_name_edit').val(full_name);
    $('#position_edit').val(position);
    $('#term_duration_edit').val(term_duration);
    $('#status_edit').val(status);
    $('#purok_edit').val(purok);

    $('#old_official_img_directory').val(official_img_directory);
}


function deleteOfficial(official_id, official_img_directory){

    Swal.fire({
        icon: 'question',
        title: 'Do you Really Want to Delete this Official?',
        text: 'This Cannot Be Undone!',
        showDenyButton: true,
        showCancelButton: true,
        showConfirmButton: false,
        denyButtonText: `Delete`,
      }).then((result) => {
          if (result.isDenied) {
            var url = "/delete_Official";

            // Construct the full URL with "id"
            document.location.href = url + "?official_id=" + official_id+ "&official_img_directory=" +official_img_directory;
        }
      })

}


$(function(){
    $('#official_image_edit').change(function(){
      var input = this;
      var url = $(this).val();
      var ext = url.substring(url.lastIndexOf('.') + 1).toLowerCase();
      if (input.files && input.files[0]&& (ext == "png" || ext == "jpeg" || ext == "jpg")) 
       {
          var reader = new FileReader();
  
          reader.onload = function (e) {
             $('#official_preview_img_edit').attr('src', e.target.result);
          }
         reader.readAsDataURL(input.files[0]);
      }
      else
      {
        $('#official_preview_img_edit').attr('src', '../static/images/map.jpg');
      }
    });
  
  });

