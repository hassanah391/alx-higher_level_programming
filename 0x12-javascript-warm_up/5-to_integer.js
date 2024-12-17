#!/usr/bin/node

const { argv } = require('node:process');

const num = +Math.floor(argv[2]);
if (typeof num === 'number' && !Number.isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
