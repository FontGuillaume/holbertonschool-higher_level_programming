-- Ce script SQL calcule la moyenne des scores dans la table 'second_table'
-- La fonction AVG() calcule la moyenne arithmétique de tous les scores
-- L'alias AS average renomme la colonne résultante pour plus de clarté
-- Cette requête permet d'obtenir rapidement une vue d'ensemble du niveau moyen des scores
SELECT AVG(score) AS average
FROM second_table;
