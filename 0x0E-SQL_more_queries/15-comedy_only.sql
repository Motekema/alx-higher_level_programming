-- lists all Comedy shows in a database hbtn_0d_tvshows
-- lists all rows of the database corresponding to the column value
SELECT title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
GROUP BY title
ORDER BY title ASC;
