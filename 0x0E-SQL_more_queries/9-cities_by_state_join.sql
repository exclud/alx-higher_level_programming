-- This script lists all cities from the cities table with their corresponding state names

-- List cities with their corresponding state names, sorted by cities.id
SELECT cities.id, cities.name, states.name AS state_name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
