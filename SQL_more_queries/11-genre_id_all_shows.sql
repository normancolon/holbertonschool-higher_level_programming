-- Script that lists all TV shows and their genre IDs, if available
SELECT 
    tv_shows.title, 
    tv_show_genres.genre_id -- Joins tv_shows with tv_show_genres using a LEFT JOIN
FROM 
    tv_shows
LEFT JOIN 
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY 
    tv_shows.title, 
    tv_show_genres.genre_id;

