-- This script lists all cities of California from the cities table
-- Find the state_id for California from the states table
SET @state_id := (SELECT id FROM states WHERE name = 'California');

-- List all cities of California sorted by cities.id
SELECT id, name
FROM cities
WHERE state_id = @state_id
ORDER BY id ASC;
