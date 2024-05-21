#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/', (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  JSON.parse(body).results[process.argv[2] - 1].characters.forEach(character => {
    request(character, (error, response, body) => {
      if (error) {
        console.error(error);
      }
      console.log(JSON.parse(body).name);
    });
  });
});
