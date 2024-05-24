// Select the HTML element with ID 'character'
const character = document.getElementById('character');

// Define the API URL for fetching the character data
const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Fetch the character data from the API using the Fetch API
fetch(apiUrl)
  // Check if the response is OK (status code 200-299) and parse the JSON data, or throw an error
  .then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Failed to fetch character data');
    }
  })
  // Display the character name in the HTML element with ID 'character'
  .then((data) => {
    const characterName = data.name;

    character.textContent = characterName;
  })
  // Log any errors that occur during the fetch or parsing process
  .catch(error => {
    console.error(error);
  });
