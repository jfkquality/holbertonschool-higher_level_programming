#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    for (let j = 0; j < this.height * 2; j++) {
      console.log('X'.repeat(this.width * 2));
    }
  }

  rotate () {
    for (let k = 0; k < this.width * 2; k++) {
      console.log('X'.repeat(this.height * 2));
    }
  }
}

module.exports = Rectangle;
