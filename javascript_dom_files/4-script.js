// Select the element with id 'add_item'
let addItemElement = document.getElementById('add_item');

// Add an event listener for the 'click' event
addItemElement.addEventListener('click', function() {
    // Create a new li element
    let newListItem = document.createElement('li');
    // Set the content of the new li element
    newListItem.textContent = 'Item';
    // Select the ul element with class 'my_list'
    let listElement = document.querySelector('ul.my_list');
    // Append the new li element to the ul element
    listElement.appendChild(newListItem);
});
