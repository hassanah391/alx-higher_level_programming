#!/usr/bin/node

const parentSquare = require('./5-square.js');

class Square extends parentSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    super.print(c);
  }
}
module.exports = Square;
