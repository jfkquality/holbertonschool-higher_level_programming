#!/usr/bin/node
if (parseInt(process.argv[2])) {
  let i = parseInt(process.argv[2]);
  const j = i;
  const x = 'X';
  while (i > 0) {
    console.log(x.repeat(j));
    i--;
  }
} else {
  console.log('Missing size');
}
