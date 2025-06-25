-- Ce script liste les émissions de télévision avec au moins un genre associé
-- Il effectue une jointure entre les tables tv_shows et tv_show_genres
-- Seules les émissions ayant au moins un genre apparaissent dans les résultats
-- Les résultats sont triés par titre d'émission et ID de genre en ordre croissant
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;