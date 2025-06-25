-- Ce script liste toutes les émissions de télévision sans genre associé
-- Il utilise une jointure externe gauche pour inclure les émissions sans genre
-- La clause WHERE filtre pour ne garder que les lignes où genre_id est NULL
-- Les résultats sont triés par titre d'émission en ordre croissant
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;