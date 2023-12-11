#!/usr/bin/node

const argument = process.argv[2];

if (!argument) {
  console.log('No argument');
} else {
  console.log(argument);
}
