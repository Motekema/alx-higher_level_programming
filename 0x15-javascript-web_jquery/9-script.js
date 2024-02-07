// Queries an API for speed in SF and replace the text of the
// div#sf_wind_speed tag with the speed

$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
