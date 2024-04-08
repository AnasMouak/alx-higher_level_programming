#!/usr/bin/node

if (parseInt(process.argv[2])) {
  let x = 0;
  while (x < parseInt(process.argv[2])) {
    console.log('C is fun');
    x++;
  }
} else {
  console.log('Missing number of occurrences');
}
