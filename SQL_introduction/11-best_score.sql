-- Ce script SQL affiche les enregistrements de 'second_table' ayant un score supérieur ou égal à 10
-- La commande SELECT récupère les colonnes score et name
-- La clause WHERE filtre les résultats pour ne montrer que les enregistrements avec un score >= 10
-- La clause ORDER BY score DESC trie les résultats du score le plus élevé au plus bas
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
