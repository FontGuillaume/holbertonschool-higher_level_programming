#!/usr/bin/node
const argv = process.argv;
if (argv[2] !== undefined && argv[3] !== undefined) {
  console.log(argv[2] + ' is ' + argv[3]);
} else if (argv[2] !== undefined) {
  console.log(argv[2] + ' is undefined');
} else {
  console.log('undefined is undefined');
}
