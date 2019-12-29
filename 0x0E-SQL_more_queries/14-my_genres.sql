-- lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use only one SELECT statement

SELECT g.name
FROM tv_genres AS g
INNER JOIN tv_show_genres AS tvsg
ON g.id = tvsg.genre_id
INNER JOIN tv_shows AS tv
ON tv.id = tvsg.show_id
WHERE tv.title = "Dexter"
ORDER BY g.name ASC
