-- This script lists genres with the number of linked shows from the hbtn_0d_tvshows database

USE hbtn_0d_tvshows;

-- List genres with the number of linked shows
SELECT tv_genres.name AS genre,
       COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
