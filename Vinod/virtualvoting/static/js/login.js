$(document).ready(function () {
    $('#login_btn').click(function () {

      //aadhar
      if ($('#aadhar').val() == '') {
          $('#aadhar_error').show();
          error = true;
      }
      else {
          $('#aadhar_error').hide();
      }

      if ($('#password').val() == '') {
          $('#password_error').show();
          error = true;
      }
      else {
          $('#password_error').hide();
      }

      if (error) {
          return;
      } else {
        $.ajax({
            url: window.location.origin + '/',
            type: 'POST',
            dataType: 'json',
            data: {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'password': $('#password').val(),
                    'aadhar': $('#aadhar').val(),
                  },
            success: function (response) {
                if (response.success == 'True') {
                    window.location.href = window.location.origin + '/cast_vote/';
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
