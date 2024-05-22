// Select header element
const header = document.querySelector('header');

// Select red header button
const redHeader = document.getElementById('red_header');

// Add click event listener to red header button
redHeader.addEventListener('click', () => {
  // Add 'red' class to header element
  header.classList.add('red');
});
