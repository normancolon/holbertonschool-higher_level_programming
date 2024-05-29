// Select the element with id 'red_header'
let redHeaderElement = document.getElementById('red_header');

// Add an event listener for the 'click' event
redHeaderElement.addEventListener('click', function() {
    // Select the header element
    let headerElement = document.querySelector('header');
    // Add the 'red' class to the header element
    headerElement.classList.add('red');
});
