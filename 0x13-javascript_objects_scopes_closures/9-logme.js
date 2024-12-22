#!/usr/bin/node

let nmArgs = 0;

exports.logMe = function (item) {
  console.log(`${nmArgs++}: ${item}`);
};
