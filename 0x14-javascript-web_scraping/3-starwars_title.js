#!/usr/bin/node

const request = new Request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], {
  method: 'GET',
  headers: new Headers({
    'Content-Type': 'application/json'
  })
});

fetch(request)
  .then(response => response.json())
  .then(data => {
    console.log(data.title);
  });
