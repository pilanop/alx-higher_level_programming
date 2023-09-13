#!/usr/bin/node
const arg = process.argv;
if (arg[2] === undefined) {
    console.log('No argument')
}
else {console.log(arg[2]);}
