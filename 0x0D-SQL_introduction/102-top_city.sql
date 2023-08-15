-- Display the top 3 if cities temp during JULY and AUGUST
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER by avg_temp DESC
LIMIT 3;
