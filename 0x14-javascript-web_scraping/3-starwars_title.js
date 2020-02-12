#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) throw (error);
  const film = JSON.parse(body);
  console.log(film.title);
});
