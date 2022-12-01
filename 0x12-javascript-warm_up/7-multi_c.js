#!/usr/bin/node

let count = 0;
const args = process.argv[2];
if (parseInt(args)) {
  while (count < args) {
    console.log('C is fun');
    count = count + 1;
  }
} else {
  console.log('Missing number of occurrences');
}
