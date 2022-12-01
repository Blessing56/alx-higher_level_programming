#!/usr/bin/node

let count = 0;
const str = 'X';
const args = process.argv[2];
const strg = str.repeat(args);

if (parseInt(args)) {
  while (count < args) {
    console.log(strg);
    count = count + 1;
  }
} else {
  console.log('Missing size');
}
