#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h === 0 || h < 0 || w === 0 || w < 0 || !h) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let x = 0;
    while (x < this.height) {
      let y = 0;
      let line = '';
      while (y < this.width) {
        line += 'X';
        y++;
      }
      console.log(line);
      x++;
    }
  }
}

module.exports = Rectangle;
