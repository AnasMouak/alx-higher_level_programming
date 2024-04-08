#!/usr/bin/node

if (process.argv.length - 2 === 0 || process.argv.length - 2 === 1) {
  console.log('0');
} else if (process.argv.length - 2 > 1) {
  const sortedArgs = process.argv.slice(2).map(Number).sort((a, b) => b - a);
  console.log(sortedArgs[1]);
}
