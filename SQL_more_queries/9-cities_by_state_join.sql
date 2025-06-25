-- Ce script liste toutes les villes contenues dans la base de données avec leur état
-- Il utilise une jointure pour associer chaque ville à son état correspondant
-- La requête affiche l'ID de la ville, le nom de la ville et le nom de l'état
-- Les résultats sont triés par ID de ville en ordre croissant
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;