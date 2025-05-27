#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId + '/';

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error: Status code ' + response.statusCode);
    return;
  }

  try {
    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;

    // Keep characters in order
    const characterNames = new Array(characterUrls.length);
    let charactersProcessed = 0;

    characterUrls.forEach((url, index) => {
      request(url, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Character request error:', charError);
          return;
        }

        if (charResponse.statusCode !== 200) {
          console.error('Character request error: Status code ' + charResponse.statusCode);
          return;
        }

        try {
          const characterData = JSON.parse(charBody);
          characterNames[index] = characterData.name;
          charactersProcessed++;

          // When all characters are processed, print them in order
          if (charactersProcessed === characterUrls.length) {
            characterNames.forEach(name => console.log(name));
          }
        } catch (parseError) {
          console.error('Error parsing character data:', parseError);
        }
      });
    });
  } catch (parseError) {
    console.error('Error parsing film data:', parseError);
  }
});
