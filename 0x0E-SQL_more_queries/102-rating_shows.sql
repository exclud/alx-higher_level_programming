-- This script lists shows by their rating sum from the hbtn_0d_tvshows_rate database
-- List shows by their rating sum
SELECT CONCAT(tv_shows.title, ' - ', IFNULL(SUM(rating), 0)) AS show_rating_sum
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY SUM(rating) DESC;
