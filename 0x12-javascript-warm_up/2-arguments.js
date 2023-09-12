#!/usr/bin/node
const argLength = process.argv.length;
if (argLength === 2) {
  console.log('No argument');
} else if (argLength === 3) {
  console.log('Argument found');
} else { console.log('Arguments found'); }
