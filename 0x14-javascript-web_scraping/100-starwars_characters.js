#!/usr/bin/node

const request = require('request');

function fetchCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) return reject(error);
      if (response.statusCode !== 200) return reject('Failed to retrieve character');

      const character = JSON.parse(body);
      resolve(character.name);
    });
  });
}

function fetchMovieCharacters (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  request(url, async (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Unexpected status code:', response.statusCode);
      return;
    }

    const film = JSON.parse(body);
    const characterUrls = film.characters;

    for (const url of characterUrls) {
      try {
        const name = await fetchCharacterName(url);
        console.log(name);
      } catch (error) {
        console.error('Error fetching character name:', error);
      }
    }
  });
}

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: node getCharacters.js <Movie ID>');
  process.exit(1);
}

fetchMovieCharacters(movieId);
