#!/usr/bin/node
function add(a, b) {
  return parseInt(a) + parseInt(b);
}
const num1 = process.argv[2];
const num2 = process.argv[3];
const result = add(num1, num2);
console.log(isNaN(result) ? 'NaN' : result);
