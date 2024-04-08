#!/usr/bin/node

if (parseInt(process.argv[2])) {
  let x = 0;
  while (x < parseInt(process.argv[2])) {
    let y = 0;
    let line = '';
    while (y < parseInt(process.argv[2])) {
      line += 'X';
      y++;
    }
    console.log(line);
    x++;
  }
} else {
  console.log('Missing size');
}
