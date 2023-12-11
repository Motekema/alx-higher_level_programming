#!/usr/bin/node
function factorial(n) {
  if (isNaN(n)) {
    return 1;
  }

  n = parseInt(n);

  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const num = process.argv[2];
const result = factorial(num);
console.log(result);
