#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) throw (error);
  const characters = JSON.parse(body).characters;
  characters.forEach(function (character, idx, arr2) {
    request(character, function (err, func, bod) {
      if (err) throw err;
      console.log(JSON.parse(bod).name);
    });
  });
});
