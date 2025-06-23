-- Ce script SQL affiche le nombre d'enregistrements pour chaque score distinct dans la table 'second_table'
-- La commande SELECT récupère le score et le nombre d'occurrences de chaque score
-- La fonction COUNT(*) compte le nombre d'enregistrements et l'alias AS number rend le résultat plus lisible
-- La clause GROUP BY score regroupe les résultats par valeur de score
-- La clause ORDER BY number DESC trie les résultats du nombre d'occurrences le plus élevé au plus bas
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC
