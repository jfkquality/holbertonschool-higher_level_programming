#!/usr/bin/node
if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
  process.exit(1);
}
const arr = process.argv.slice(2);
const max = Math.max.apply(null, arr);
arr.splice(arr.indexOf(max.toString()), 1);
const max2 = Math.max.apply(null, arr);
console.log(max2);
