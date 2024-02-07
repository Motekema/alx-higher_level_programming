//To achieve this task using the jQuery API, create a JavaScript file

$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
