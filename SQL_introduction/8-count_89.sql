-- Ce script SQL compte le nombre d'enregistrements dans la table 'first_table' où l'id est égal à 89
-- La fonction COUNT(*) renvoie le nombre total de lignes qui correspondent à la condition
-- La clause WHERE filtre les résultats pour ne compter que les lignes où id=89
-- Cette requête est utile pour vérifier rapidement combien d'entrées correspondent à un critère spécifique
SELECT COUNT(*) FROM first_table WHERE id = 89;
