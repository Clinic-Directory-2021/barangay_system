
$('#addResidentForm').on('submit', function(e){

    $('#addResidentBtn').prop('disabled', true);
    e.preventDefault();
    console.log("1");

    var formData = new FormData();
    var files = $('#resident_image')[0].files[0];
  
    formData.append('resident_image', files);
    formData.append('fileName', files.name);

    formData.append('first_name', $('#first_name').val());
    formData.append('email', $('#email').val());
    formData.append('middle_name', $('#middle_name').val());
    formData.append('street', $('#street').val());
    formData.append('last_name', $('#last_name').val());
    formData.append('purok', $('#purok').val());
    formData.append('gender', $('#gender').val());
    formData.append('citizenship', $('#citizenship').val());
    formData.append('civil_status', $('#civil_status').val());
    formData.append('diff_disabled', $('#diff_disabled').val());
    formData.append('age', $('#age').val());
    formData.append('relation', $('#relation').val());
    formData.append('birthdate', $('#birthdate').val());
    formData.append('religion', $('#religion').val());
    formData.append('phone_number', $('#phone_number').val());
    formData.append('status', $('#status').val());
    formData.append('csrfmiddlewaretoken', $("input[name='csrfmiddlewaretoken']").val());

    $.ajax({
        type: 'post',
        url: "/addResident/",
        data: formData,
        enctype: 'multipart/form-data',
        processData: false,
        contentType: false,
        success: function(data){
            addResidentSuccess(data);
        },
        error: function(data){
            $('#addResidentBtn').prop('disabled', false);
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
              })
        },
  
    });
});

$(function(){
    $('#resident_image').change(function(){
      var input = this;
      var url = $(this).val();
      var ext = url.substring(url.lastIndexOf('.') + 1).toLowerCase();
      if (input.files && input.files[0]&& (ext == "png" || ext == "jpeg" || ext == "jpg")) 
       {
          var reader = new FileReader();
  
          reader.onload = function (e) {
             $('#resident_preview_img').attr('src', e.target.result);
          }
         reader.readAsDataURL(input.files[0]);
      }
      else
      {
        $('#resident_preview_img').attr('src', '../static/images/map.jpg');
      }
    });
  
  });

function addResidentSuccess(data){
    if(data=="Email Already Exists!"){
        $('#addResidentBtn').prop('disabled', false);
         Swal.fire({
            icon: 'error',
            title: 'Email Already Exists!',
            confirmButtonText: 'OKAY',
          })
    }else if (data == 'Success!'){
        $('#addResidentBtn').prop('disabled', false);
        Swal.fire({
            icon: 'success',
            title: 'Resident Successfully Added!',
            confirmButtonText: 'OKAY',
          })
    }
}