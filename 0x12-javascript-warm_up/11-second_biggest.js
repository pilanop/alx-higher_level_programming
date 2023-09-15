#!/usr/bin/node
const arg = process.argv;
const newArg = arg.slice(2);
const parsedArg = []
for (let i = 0; i < newArg.length; i++) {
   parsedArg.push(parseInt(newArg[i]));
}
parsedArg.sort();
if (arg.length <= 3) {
  console.log(0);
} else {
  console.log(parsedArg[parsedArg.length - 2]);
}
