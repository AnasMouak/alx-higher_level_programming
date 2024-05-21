#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  let count = 0;

  JSON.parse(body).results.forEach(result => {
    result.characters.forEach(character => {
      if (character === 'https://swapi-api.alx-tools.com/api/people/18/') {
        count++;
      }
    });
  });
  console.log(count);
});
