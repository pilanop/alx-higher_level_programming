#!/usr/bin/node
const arg = process.argv;
const newArg = [];
for (let i = 2; i < arg.length; i++) {
  newArg.push(parseInt(arg[i]));
}
newArg.sort();
if (arg[2] === undefined || arg.length === 3) {
  console.log(0);
} else {
  console.log(newArg[newArg.length - 2]);
}
