const { channel } = require('diagnostics_channel');
const request = require('request');


request('https://swapi-api.alx-tools.com/api/films/3', function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    characters = JSON.parse(body)["characters"];
    characters.forEach(character => {
      request(character, function (error, response, body) {
        if (error) {
          console.error('Error:', error);
        } else {
          console.log(SON.parse(body)["name"]);
        }
      });
    });
    
  }
});