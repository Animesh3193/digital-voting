$(document).ready(function () {
    $('#register_btn').click(function () {

      //name
      if ($('#name').val() == '') {
          $('#name_error').show();
          error = true;
      }
      else {
          $('#name_error').hide();
      }

      //last name
      if ($('#last_name').val() == '') {
          $('#last_name_error').show();
          error = true;
      }
      else {
          $('#last_name_error').hide();
      }

      //aadhar
      if ($('#aadhar').val() == '') {
          $('#aadhar_error').show();
          error = true;
      }
      else {
          $('#aadhar_error').hide();
      }

      //Date_of_birth
        if ($('#Date_of_birth').val() == '') {
            $('#Date_of_birth_error').show();
            error = true;
        } else {
            $('#Date_of_birth_error').hide();
        }

      //password
      if ($('#password').val() == '') {
          $('#password_error').show();
          error = true;
      }
      else {
          $('#password_error').hide();
      }

      //password2
      if ($('#password2').val() == '') {
          $('#password2_error').show();
          error = true;
      }
      else {
          $('#password2_error').hide();
      }

      if (error) {
          return;
      } else {
        $.ajax({
            url: window.location.origin + '/register/',
            type: 'POST',
            dataType: 'json',
            data: {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'name':$('#name').val(),
                    'last_name':$('#last_name').val(),
                    'aadhar': $('#aadhar').val(),
                    'Date_of_birth': $('#Date_of_birth').val(),
                    'password': $('#password').val(),
                    'password2':$('#password2').val()
                  },
            success: function (response) {
                if (response.success == 'True') {
                    window.location.href = window.location.origin + '/';
                } else {
                    alert(response);
                }
            },
            error: function (response) {
              }
      });
    };
});
});
