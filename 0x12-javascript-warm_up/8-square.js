#!/Users/khalidmohammed/.nvm/versions/node/v18.17.0/bin/node
const arg = process.argv;
if (isNaN(arg[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg[2]; i++) {
    for (let j = 0; j < arg[2]; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
