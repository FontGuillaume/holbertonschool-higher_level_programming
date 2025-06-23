-- Ce script SQL affiche tous les enregistrements de la table 'second_table' triés par score décroissant
-- La commande SELECT avec les colonnes spécifiées (score, name) renvoie uniquement ces deux colonnes
-- FROM second_table indique la table source des données
-- La clause ORDER BY score DESC trie les résultats du score le plus élevé au plus bas
SELECT score, name
FROM second_table
ORDER BY score DESC;
