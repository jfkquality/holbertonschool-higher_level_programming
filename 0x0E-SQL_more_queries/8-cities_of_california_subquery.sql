-- lists all the cities of California that can be found in the database hbtn_0d_usa.
-- The states table contains only one record where name = California
-- (but the id can be different, as per the example)
-- Results must be sorted in ascending order by cities.id
-- You are not allowed to use the JOIN keyword
-- The database name will be passed as an argument of the mysql command
SELECT c.id, c.name
FROM cities AS c
WHERE states_id in
      SELECT if from states where name = 'California'

-- Don't need JOIN; can use subquery (complete above. See Gary's)
INNER JOIN states AS s
ON c.state_id = s.id
WHERE s.name = 'California'
ORDER BY c.id ASC
