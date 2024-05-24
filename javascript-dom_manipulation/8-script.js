// Define a function to fetch and display the translation of 'hello'
const fetchHello = () => {
  // Select the HTML element with ID 'hello'
  const helloElement = document.getElementById('hello');

  // Define the API URL for fetching the translation of 'hello'
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Fetch the translation of 'hello' from the API using the Fetch API
  fetch(apiUrl)
    // Parse the JSON data from the response
    .then(response => response.json())
    // Display the translation of 'hello' in the HTML element with ID 'hello'
    .then(data => {
      // Get the translation of 'hello' from the data object
      const helloTranslation = data.hello;

      // Set the text content of the HTML element with ID 'hello' to the translation of 'hello'
      helloElement.textContent = helloTranslation;
    })
    // Log any errors that occur during the fetch or parsing process
    .catch(error => {
      console.error(error);
    });
};

// Wait for the DOM to be fully loaded before fetching and displaying the translation of 'hello'
document.addEventListener('DOMContentLoaded', fetchHello);
