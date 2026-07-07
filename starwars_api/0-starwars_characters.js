#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  const printCharacter = (index) => {
    if (index === characters.length) {
      return;
    }

    request(characters[index], (err, res, data) => {
      if (err) {
        console.error(err);
        return;
      }

      const character = JSON.parse(data);
      console.log(character.name);

      printCharacter(index + 1);
    });
  };

  printCharacter(0);
});
