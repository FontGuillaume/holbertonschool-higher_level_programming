-- Ce script liste tous les genres de la série "Dexter"
-- Il utilise des jointures entre les tables tv_shows, tv_show_genres et tv_genres
-- Les résultats affichent uniquement les noms des genres associés à cette série
-- Les genres sont triés par ordre alphabétique croissant
SELECT tv_genres.name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name ASC;
