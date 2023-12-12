#!/usr/bin/node
/* Define a class Rectangle with constructor */

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if width or height is not a positive integer
      return {};
    }
  }
}

module.exports = Rectangle;
