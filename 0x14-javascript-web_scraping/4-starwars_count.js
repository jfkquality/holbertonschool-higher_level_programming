#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) throw (error);
  const res = JSON.parse(body);
  const films = res.results;
  const wedge = 'https://swapi.co/api/people/18/';
  let count = 0;
  films.forEach(function (film, index, arr) {
    if (film.characters.indexOf(wedge) >= 0) {
      count++;
    }
  });
  // for (const film of films) {
  //   const characters = film.characters;
  //   for (const character of characters) {
  //     if (character.includes(wedge)) {
  //       count++;
  //     }
  //   }
  // }
  console.log(count);
});
