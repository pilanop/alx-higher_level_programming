#!/usr/bin/node
function add (a, b) {
  return parseInt(a) + parseInt(b);
}
const arg = process.argv;
console.log(add(arg[2], arg[3]));
