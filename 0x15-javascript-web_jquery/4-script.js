// Toggles class of HTML tag 'HEADER' when the user clicks the
// div#toggle_header tag

$('div#toggle_header').click(function () {
    $('header').ToggleClass('red');
  });
