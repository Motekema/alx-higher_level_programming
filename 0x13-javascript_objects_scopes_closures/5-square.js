#!/usr/bin/node
/* Define a class Square that inherits from Rectangle */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    // Call the constructor of the base class (Rectangle) with size for both width and height
    super(size, size);
  }
}

module.exports = Square;
