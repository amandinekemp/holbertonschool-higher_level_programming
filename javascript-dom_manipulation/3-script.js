// Get the toggle header button
const toggleHeader = document.getElementById('toggle_header');

// Get the header element
const header = document.querySelector('header');

// Add a click event listener to the toggle header button
toggleHeader.addEventListener('click', function () {
  // If the header is red, change it to green
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  // If the header is green, change it to red
  } else if (header.classList.contains('green')) {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
