#!/usr/bin/node
const request = require('request');

const film = process.argv.slice(2)[0];
request('https://swapi-api.alx-tools.com/api/films/' + film, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    const characters = JSON.parse(body).characters;
    const names = characters.map(
      character => new Promise((resolve, reject) => {
        request(character, function (error, response, body) {
          if (error) {
            reject(error)
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      })
    );
    Promise.all(names)
      .then(n => console.log(n.join('\n')))
      .catch(err => console.log(err));
  }

});
