
$(function(){
    $('#official_image').change(function(){
      var input = this;
      var url = $(this).val();
      var ext = url.substring(url.lastIndexOf('.') + 1).toLowerCase();
      if (input.files && input.files[0]&& (ext == "png" || ext == "jpeg" || ext == "jpg")) 
       {
          var reader = new FileReader();
  
          reader.onload = function (e) {
             $('#official_preview_img').attr('src', e.target.result);
          }
         reader.readAsDataURL(input.files[0]);
      }
      else
      {
        $('#official_preview_img').attr('src', '../static/images/map.jpg');
      }
    });
  
  });