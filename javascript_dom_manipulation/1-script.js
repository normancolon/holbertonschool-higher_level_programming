// Select the element with id 'red_header'
let redHeaderElement = document.getElementById('red_header');

// Add an event listener for the 'click' event
redHeaderElement.addEventListener('click', function() {
    // Select the header element
    let headerElement = document.querySelector('header');
    // Update the text color to red (#FF0000)
    headerElement.style.color = '#FF0000';
});
