-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
SELECT tv.title, tvsg.genre_id
FROM tv_shows AS tv
INNER JOIN tv_show_genres AS tvsg
ON tv.id = tvsg.show_id
ORDER BY tv.title ASC
-- tvsg.id ASC
