// Select the element with id 'update_header'
let updateHeaderElement = document.getElementById('update_header');

// Add an event listener for the 'click' event
updateHeaderElement.addEventListener('click', function() {
    // Select the header element
    let headerElement = document.querySelector('header');
    // Update the text content of the header element
    headerElement.textContent = 'New Header!!!';
});
