#!/usr/bin/node
const request = require('request');

const film = process.argv.slice(2)[0];
request('https://swapi-api.alx-tools.com/api/films/' + film, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach(character => {
      request(character, function (error, response, body) {
        if (error) {
          console.error('Error:', error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
