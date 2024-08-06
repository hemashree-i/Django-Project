$(document).ready(function () {
  // $('#uploading_image').change(function () {
  //   var file = $(this)[0].files[0];
  //   console.log(file.name)
  // });

  $('#imageUploadForm').on('submit', function (e) {
    var file = $('#uploading_image')[0].files[0];
    console.log(file.name)
    e.preventDefault()
    var formData = new FormData();
    formData.append('file', file);
    console.log(file)

    try {
      $.ajax({
        url: 'imageuploading',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function (response) {
          // Handle success response here
          console.log('File uploaded successfully:', response);
          alert(response)
        },
        error: function (xhr, status, error) {
          // Handle error response here
          console.error('Error uploading file:', error);
        }
      });
    }
    catch (error) {
      console.log(error);
    }
  });
});
