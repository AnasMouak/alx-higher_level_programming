#!/usr/bin/node

const request = require('request');

function fetchCharacterName(url, callback) {
  request(url, (error, response, body) => {
    if (error) {
      callback(error);
      return;
    }
    const character = JSON.parse(body);
    callback(null, character.name);
  });
}

function fetchCharactersInOrder(characters, index) {
  if (index >= characters.length) {
    return;
  }
  fetchCharacterName(characters[index], (error, name) => {
    if (error) {
      console.error(error);
      return;
    }
    console.log(name);
    fetchCharactersInOrder(characters, index + 1);
  });
}

request('https://swapi-api.alx-tools.com/api/films/', (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const filmIndex = process.argv[2] - 1;
  const films = JSON.parse(body).results;
  const characters = films[filmIndex].characters;
  fetchCharactersInOrder(characters, 0);
});
