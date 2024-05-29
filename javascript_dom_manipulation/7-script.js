// Fetch the list of movies from the provided URL
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json()) // Parse the JSON from the response
    .then(data => {
        // Select the ul element with id 'list_movies'
        let listMoviesElement = document.getElementById('list_movies');
        // Iterate through the results and create a list item for each movie title
        data.results.forEach(movie => {
            let listItem = document.createElement('li');
            listItem.textContent = movie.title;
            listMoviesElement.appendChild(listItem);
        });
    })
    .catch(error => console.error('Error:', error)); // Log any errors to the console
