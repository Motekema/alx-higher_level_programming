#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);

    const completedTasks = tasks.reduce((result, task) => {
      if (task.completed) {
        if (result[task.userId]) {
          result[task.userId]++;
        } else {
          result[task.userId] = 1;
        }
      }
      return result;
    }, {});

    console.log(completedTasks);
  }
});
