#!/usr/bin/node

const dict = require('./101-data').dict;

console.log(Object.entries(dict)
  .reduce((acc, [key, value]) => {
    acc[value] = acc[value] || [];
    acc[value].push(key);
    return acc;
  }, {}));
