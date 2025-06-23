-- Ce script SQL supprime tous les enregistrements avec un score inférieur ou égal à 5 dans la table 'second_table'
-- La commande DELETE FROM supprime des lignes entières de la table
-- La clause WHERE filtre les enregistrements pour ne supprimer que ceux avec un score <= 5
-- Cette requête permet de "nettoyer" la table en supprimant les scores les plus bas
DELETE FROM second_table
WHERE score <= 5;
