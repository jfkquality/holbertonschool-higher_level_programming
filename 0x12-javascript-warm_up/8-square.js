#!/usr/bin/node
// if (Number.isInteger(process.argv[2])) {
if (parseInt(process.argv[2])) {
  let i = process.argv[2];
  let j = i;
  let x = 'x';
  while (i > 0) {
    console.log(x.repeat(j));
    i--;
  }
} else {
  console.log('Missing size');
}
