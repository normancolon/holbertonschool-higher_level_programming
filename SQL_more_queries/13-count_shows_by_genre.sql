-- Counts shows per genre, sorted by count and genre ID
SELECT g.name AS genre, COUNT(s.genre_id) AS number_of_shows
FROM tv_show_genres s
JOIN tv_genres g ON g.id = s.genre_id
GROUP BY s.genre_id
ORDER BY number_of_shows DESC, g.id ASC;
