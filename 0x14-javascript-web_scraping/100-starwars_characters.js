#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;

    // Function to get character names from URLs
    const getCharacterName = (characterUrl) => new Promise((resolve) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        }
      });
    });

    // Fetch and print character names
    Promise.all(charactersUrls.map(getCharacterName))
      .then((characterNames) => {
        characterNames.forEach((name) => console.log(name));
      })
      .catch((err) => console.error(err));
  }
});
