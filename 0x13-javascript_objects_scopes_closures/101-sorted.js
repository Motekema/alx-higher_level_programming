#!/usr/bin/node
const { dict } = require('./101-data');

const sortedDict = {};

Object.keys(dict).forEach(userId => {
  const occurrences = dict[userId];

  if (sortedDict[occurrences] === undefined) {
    sortedDict[occurrences] = [userId];
  } else {
    sortedDict[occurrences].push(userId);
  }
});

console.log(sortedDict);
