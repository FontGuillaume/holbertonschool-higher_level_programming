-- Ce script compte le nombre d'émissions pour chaque genre dans la base de données
-- Il effectue une jointure entre les tables tv_genres et tv_show_genres
-- Les résultats sont groupés par genre et comptent le nombre d'émissions associées
-- Seuls les genres liés à au moins une émission sont inclus dans les résultats
-- Les résultats sont triés par nombre d'émissions en ordre décroissant
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;