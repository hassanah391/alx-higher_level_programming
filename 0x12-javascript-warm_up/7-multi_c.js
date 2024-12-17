#!/usr/bin/node

const { argv } = require('node:process');

let x = argv[2];

if (typeof x === 'undefined') {
  console.log('Missing number of occurrences');
  x = +x;
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
