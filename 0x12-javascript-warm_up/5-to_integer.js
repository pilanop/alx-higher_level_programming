#!/usr/bin/node
const arg = process.argv;
const toInt = parseInt(arg[2]);
if (isNaN(toInt)) {
  console.log('Not a number');
} else { console.log('My number: ' + toInt); }
