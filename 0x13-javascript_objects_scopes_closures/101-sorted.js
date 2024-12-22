#!/usr/bin/node

const dict = require('./101-data').dict;

const result = {};

// Iterate through each user ID and its occurrence count
for (const userId in dict) {
  const occurrence = dict[userId];
  if (!result[occurrence]) {
    result[occurrence] = [];
  }
  result[occurrence].push(userId);
}

console.log(result);
