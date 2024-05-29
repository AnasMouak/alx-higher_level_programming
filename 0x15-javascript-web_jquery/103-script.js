$(document).ready(function () {
  function translate () {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + $('#language_code').val(), function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').on('click', translate);

  $('#language_code').on('keypress', function (e) {
    if (e.which === 13) {
      translate();
    }
  });
});
