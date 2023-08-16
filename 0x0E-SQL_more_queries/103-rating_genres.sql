-- This script lists genres by their rating sum from the hbtn_0d_tvshows_rate database
-- List genres by their rating sum
SELECT CONCAT(tv_genres.name, ' - ', IFNULL(SUM(rating), 0)) AS genre_rating_sum
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY SUM(rating) DESC;
