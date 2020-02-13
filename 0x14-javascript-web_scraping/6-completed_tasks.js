#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) throw (error);
  const todos = JSON.parse(body);

  let results = {};

  todos.forEach(function (todo, index, arr) {
    if (!results[todo.userId]) {
      console.log("First userId: " + todo.userId);
      results[todo.userId] = 1;
    } else {
      console.log('Increment userId: ' + todo.userId + ' count ' + results[todo.userId]);
      results[todo.userId] += 1;
    }
  });
  console.log(results);
});
