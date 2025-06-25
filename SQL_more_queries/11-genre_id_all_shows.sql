-- Ce script liste toutes les émissions de télévision avec leurs genres associés
-- Il utilise une jointure externe gauche pour inclure les émissions sans genre
-- Pour les émissions sans genre, la valeur de genre_id est NULL
-- Les résultats sont triés par titre d'émission et ID de genre en ordre croissant
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;