#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  fs.writeFile(process.argv[3], body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
