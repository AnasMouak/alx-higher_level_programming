#!/usr/bin/node

const Square2 = require('./5-square');

class Square extends Square2 {
  charPrint (c) {
    if (c) {
      let x = 0;
      while (x < this.height) {
        let y = 0;
        let line = '';
        while (y < this.width) {
          line += c;
          y++;
        }
        console.log(line);
        x++;
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
