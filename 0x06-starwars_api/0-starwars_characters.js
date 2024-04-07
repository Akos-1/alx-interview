#!/usr/bin/node

const fetch = require('node-fetch');

async function getMovieCharacters(movieId) {
    const url = `https://swapi.dev/api/films/${movieId}/`;

    try {
        const response = await fetch(url);
        const movieData = await response.json();
        const characterUrls = movieData.characters;

        const characterNames = await Promise.all(
            characterUrls.map(async (characterUrl) => {
                const characterResponse = await fetch(characterUrl);
                const characterData = await characterResponse.json();
                return characterData.name;
            })
        );

        return characterNames;
    } catch (error) {
        console.error(`Error fetching data from API: ${error}`);
        return null;
    }
}
