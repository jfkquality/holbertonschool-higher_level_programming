#!/usr/bin/node
const i = parseInt(process.argv[2]);
const j = parseInt(process.argv[3]);
add(i, j);

function add (a, b) {
  console.log(a + b);
}
