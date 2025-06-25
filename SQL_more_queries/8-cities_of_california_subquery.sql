-- Ce script liste toutes les villes de Californie présentes dans la base de données
-- Il utilise une sous-requête pour récupérer l'ID de l'état de Californie
-- Les résultats sont triés par ID de ville en ordre croissant
-- La sous-requête évite d'avoir à connaître l'ID exact de la Californie
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;