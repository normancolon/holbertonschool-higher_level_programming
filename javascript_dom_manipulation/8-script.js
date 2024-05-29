// Function to fetch and display the greeting
function fetchGreeting() {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(response => response.json()) // Parse the JSON from the response
        .then(data => {
            // Select the element with id 'hello'
            let helloElement = document.getElementById('hello');
            // Update the text content with the greeting
            helloElement.textContent = data.hello;
        })
        .catch(error => console.error('Error:', error)); // Log any errors to the console
}

// Fetch the greeting when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', fetchGreeting);
