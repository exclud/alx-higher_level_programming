-- This script lists shows and linked genres from the hbtn_0d_tvshows database

-- USE hbtn_0d_tvshows;

-- List shows and linked genres
SELECT CONCAT(tv_shows.title, ' - ', IFNULL(tv_genres.name, 'NULL')) AS show_genre
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
