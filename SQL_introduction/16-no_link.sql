-- Ce script SQL affiche les enregistrements de la table 'second_table' ayant un nom non vide
-- La commande SELECT récupère les colonnes score et name
-- La clause WHERE filtre les résultats pour exclure les enregistrements où name est NULL ou vide
-- La condition IS NOT NULL vérifie l'absence de valeur NULL et name != '' vérifie que la chaîne n'est pas vide
-- La clause ORDER BY score DESC trie les résultats du score le plus élevé au plus bas
SELECT score, name 
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
