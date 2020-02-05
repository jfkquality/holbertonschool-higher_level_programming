#!/usr/bin/node
// if (Number.isInteger(process.argv[2])) {
if (parseInt(process.argv[2])) {
  let i = process.argv[2];
  while (i > 0) {
    console.log('C is fun');
    i--;
  }
} else {
  console.log('Missing number of occurrences');
}
