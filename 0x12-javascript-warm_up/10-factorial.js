#!/usr/bin/node

const { argv } = require('node:process');

function fact (n) {
  if (isNaN(n) || n < 0) {
    n = 1;
  }
  if (n === 1 || n === 0) {
    return 1;
  }
  return n * fact(n - 1);
}

console.log(fact(argv[2]));
