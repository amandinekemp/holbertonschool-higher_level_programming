// Select the HTML element with ID 'update_header'
const updateHeader = document.getElementById('update_header');

// Select the HTML element with tag 'header'
const header = document.querySelector('header');

// Add a click event listener to the 'update_header' element
updateHeader.addEventListener('click', () => {
  // Update the text content of the 'header' element to 'New Header!!!'
  header.textContent = 'New Header!!!';
});
