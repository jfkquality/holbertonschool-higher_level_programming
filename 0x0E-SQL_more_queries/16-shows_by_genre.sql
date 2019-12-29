-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
-- You can use only one SELECT statement

SELECT tv.title, g.name
FROM tv_shows AS tv
LEFT JOIN tv_show_genres AS tvsg
ON tv.id = tvsg.show_id
LEFT JOIN tv_genres AS g
ON g.id = tvsg.genre_id
ORDER BY tv.title ASC, g.name ASC
