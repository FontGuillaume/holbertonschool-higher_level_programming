-- Ce script liste toutes les émissions de télévision et leurs genres associés
-- Il utilise des jointures externes gauches pour inclure toutes les émissions
-- Même les émissions sans genre et les genres sans émission sont inclus
-- Pour les émissions sans genre, la valeur du nom de genre est NULL
-- Les résultats sont triés par titre d'émission et nom de genre en ordre croissant
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name ASC

