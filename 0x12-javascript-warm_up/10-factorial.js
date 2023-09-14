#!/usr/bin/node
const arg = process.argv;

function factorial (n) {
  if (isNaN(n) || n === 1 || n === 0) {
    return 1;
  }
  return parseInt(n) * (factorial(parseInt(n) - 1));
}

console.log(factorial(arg[2]));
