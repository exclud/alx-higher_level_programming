-- This script lists shows without the genre Comedy from the hbtn_0d_tvshows database

-- Get the genre_id for the Comedy genre
SET @comedy_genre_id := (SELECT id FROM tv_genres WHERE name = 'Comedy');

-- List shows without the genre Comedy
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id AND tv_show_genres.genre_id = @comedy_genre_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;
