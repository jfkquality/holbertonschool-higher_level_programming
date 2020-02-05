#!/usr/bin/node
// if (Number.isInteger(process.argv[2])) {
if (parseInt(process.argv[2])) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
