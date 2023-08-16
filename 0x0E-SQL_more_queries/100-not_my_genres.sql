-- This script lists genres not linked to the show Dexter from the hbtn_0d_tvshows database
-- Get the genre_id linked to the show Dexter
SET @dexter_genre_id := (SELECT genre_id FROM tv_show_genres
                         JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
                         WHERE tv_shows.title = 'Dexter');

-- List genres not linked to the show Dexter
SELECT name
FROM tv_genres
WHERE id <> @dexter_genre_id OR id IS NULL
ORDER BY name ASC;
