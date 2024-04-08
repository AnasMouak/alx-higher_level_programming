#!/usr/bin/node

function add (a, b) {
  a = parseInt(process.argv[2]);
  b = parseInt(process.argv[3]);
  const result = a + b;

  console.log(result);
  return result;
}
add(process.argv[2], process.argv[3]);
