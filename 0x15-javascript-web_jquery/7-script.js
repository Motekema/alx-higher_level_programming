// Fetched and replaced the name of the API data then replaced the name
// Of the character in the DIV#character tag text

let url = 'https://swapi.co/api/people/5/?format=json';
$.get(url, function (data, stat) {
  $('div#character').text(data.name);
});
