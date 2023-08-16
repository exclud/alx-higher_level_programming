-- Script lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

USE hbtn_0d_tvshows;

-- List shows with linked genres
SELECT CONCAT(tv_shows.title, '-', tv_show_genres_id) AS tv_show_genre
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genre.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
