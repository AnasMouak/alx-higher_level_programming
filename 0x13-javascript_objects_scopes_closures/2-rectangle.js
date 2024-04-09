#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h === 0 || h < 0 || w === 0 || w < 0 || !h) {
      return;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
