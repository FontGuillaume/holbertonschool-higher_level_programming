-- Ce script liste toutes les émissions de comédie présentes dans la base de données
-- Il utilise des jointures entre les tables tv_shows, tv_show_genres et tv_genres
-- La clause WHERE filtre pour ne récupérer que les émissions du genre "Comedy"
-- Les résultats sont triés par titre d'émission en ordre alphabétique croissant
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title ASC;
