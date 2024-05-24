// Select the HTML element with ID 'list_movies'
const listMovies = document.getElementById('list_movies');

const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Fetch the movie data from the API using the Fetch API
fetch(apiUrl)
  // Parse the JSON data from the response
  .then(response => response.json())
  // Display the movie titles in the HTML element with ID 'list_movies'
  .then(data => {
    // Get the array of movies from the data object
    const movies = data.results;
    // Loop through the array of movies
    for (const movie of movies) {
      // Create a new list item element for the movie title
      const listItem = document.createElement('li');
      // Set the text content of the list item to the movie title
      listItem.textContent = movie.title;
      // Append the list item to the HTML element with ID 'list_movies'
      listMovies.appendChild(listItem);
    }
  })
  // Log any errors that occur during the fetch or parsing process
  .catch(error => {
    console.error(error);
  });
