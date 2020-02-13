#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) throw (error);
  const todos = JSON.parse(body);

  const results = {};

  todos.forEach(function (todo, index, arr) {
    if (todo.completed) {
      if (!results[todo.userId]) {
        results[todo.userId] = 1;
      } else {
        results[todo.userId] += 1;
      }
    }
  });
  console.log(results);
});
