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

  rotate () {
    const n = this.width;
    this.width = this.height;
    this.height = n;
  }

  double () {
    const n = this.width * 2;
    const d = this.height * 2;
    this.width = n;
    this.height = d;
  }
}

module.exports = Rectangle;
