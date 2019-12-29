-- lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement

SELECT s.title
FROM tv_shows AS tv
INNER JOIN tv_show_genres AS tvsg
ON tv.id = tvsg.show_id
INNER JOIN tv_genres AS g
ON g.id = tvsg.genre_id
WHERE g.name = "Comedy"
ORDER BY tv.title ASC
