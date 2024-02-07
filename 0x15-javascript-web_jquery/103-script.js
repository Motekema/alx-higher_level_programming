//To accomplish this task using the jQuery API, you can modify the script to handle both

$(document).ready(function () {
  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function(event) {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });
});
