#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) throw (error);
  const res = JSON.parse(body);
  console.log(res);
  // const films = res.results;
  // const wedge = 'https://swapi.co/api/people/18/';
  // let count = 0;
  // for (const film in films) {
  //   const characters = films[film].characters;
  //   for (const character in characters) {
  //     if (characters[character].includes(wedge)) {
  //       count++;
  //     }
  //   }
  // }
  // console.log(count);
});
