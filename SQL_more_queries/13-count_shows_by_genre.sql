-- Lists all TV shows without an associated genre
SELECT 
    tv_shows.title, 
    tv_show_genres.genre_id -- Ensures only shows without genres are selected
FROM 
    tv_shows
LEFT JOIN 
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE 
    tv_show_genres.genre_id IS NULL
ORDER BY 
    tv_shows.title;
