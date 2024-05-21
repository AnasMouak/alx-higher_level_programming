#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const count = {};
  JSON.parse(body).forEach(result => {
    if (result.completed) {
      if (count[result.userId]) {
        count[result.userId]++;
      } else {
        count[result.userId] = 1;
      }
    }
  });
  console.log(count);
});
