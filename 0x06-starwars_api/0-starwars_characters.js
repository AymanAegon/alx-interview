const request = require('request');


request('https://swapi-api.alx-tools.com/api/films/3', function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log(body["name"]);
    // console.log('Body:', body);
  }
});