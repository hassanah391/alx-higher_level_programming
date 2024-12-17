#!/usr/bin/node

const { argv } = require('node:process');

const size = +argv[2];

if (!Number.isNaN(size)) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
