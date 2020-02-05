#!/usr/bin/node
if (parseInt(process.argv[2])) {
  const i = parseInt(process.argv[2]);
  console.log(factorial(i));
} else {
  console.log(1);
}

function factorial (a) {
  if (a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
