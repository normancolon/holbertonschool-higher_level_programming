-- Lists genres and the count of associated TV shows
SELECT 
    tv_genres.name AS genre, 
    COUNT(tv_show_genres.genre_id) AS number_of_shows -- Joins tv_genres with tv_show_genres and counts shows per genre
FROM 
    tv_show_genres
JOIN 
    tv_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY 
    tv_genres.id
ORDER BY 
    number_of_shows DESC, 
    tv_genres.id ASC;
