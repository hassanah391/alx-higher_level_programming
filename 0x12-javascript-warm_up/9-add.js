#!/usr/bin/node

const { argv } = require('node:process');

function add (a, b) {
  return a + b;
}

const a = +argv[2]; const b = +argv[3];

console.log(add(a, b));
