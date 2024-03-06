-- Script that lists genres along with the count of associated TV shows
SELECT 
    tv_genres.name AS genre, 
    COUNT(tv_show_genres.show_id) AS number_of_shows -- Counts shows per genre
FROM 
    tv_show_genres
JOIN 
    tv_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY 
    genre
ORDER BY 
    number_of_shows DESC, 
    tv_genres.id ASC;
