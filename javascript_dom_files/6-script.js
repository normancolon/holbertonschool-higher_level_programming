// Fetch the character name from the provided URL
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json()) // Parse the JSON from the response
    .then(data => {
        // Select the element with id 'character'
        let characterElement = document.getElementById('character');
        // Update the text content with the character name
        characterElement.textContent = data.name;
    })
    .catch(error => console.error('Error:', error)); // Log any errors to the console
