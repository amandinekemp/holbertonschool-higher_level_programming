// Select header element
const header = document.querySelector('header');

// Select element with ID "red_header"
const redHeader = document.querySelector('#red_header');

// Add click event listener to redHeader element
redHeader.addEventListener('click', () => {
  // Set header text color to red when event is triggered
  header.style.color = '#FF0000';
});
