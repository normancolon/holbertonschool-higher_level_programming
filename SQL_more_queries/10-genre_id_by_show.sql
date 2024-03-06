-- Script that lists all TV shows and their associated genre IDs
SELECT 
    tv_shows.title, 
    tv_show_genres.genre_id -- Joins tv_shows with tv_show_genres
FROM 
    tv_shows
JOIN 
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY 
    tv_shows.title, 
    tv_show_genres.genre_id;
