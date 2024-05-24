// Select the HTML element with ID 'add_item'
const addItem = document.getElementById('add_item');

// Select the HTML element with class 'my_list'
const myList = document.querySelector('.my_list');

// Add a click event listener to the 'add_item' element
addItem.addEventListener('click', () => {
  // Create a new 'li' element
  const newItem = document.createElement('li');

  // Set the text content of the new 'li' element to 'Item'
  newItem.textContent = 'Item';

  // Append the new 'li' element to the 'my_list' element
  myList.appendChild(newItem);
});
