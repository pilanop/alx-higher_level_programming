#!/Users/khalidmohammed/.nvm/versions/node/v18.17.0/bin/node
const arg = process.argv;
if (isNaN(arg[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arg[2]; i++) {
    console.log('C is fun');
  }
}
