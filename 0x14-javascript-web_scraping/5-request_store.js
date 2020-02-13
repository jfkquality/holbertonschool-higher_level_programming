#!/usr/bin/node
const fs = require('fs');
const Request = require('request');
const url = process.argv[2];
const fn = process.argv[3];

Request(url, function (error, response, body) {
  if (error) throw error;
  fs.writeFile(fn, body, 'utf-8', (err) => {
    if (err) console.log(err);
  });
});
