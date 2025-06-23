-- Ce script SQL met à jour le score de Bob dans la table 'second_table'
-- La commande UPDATE modifie les données existantes dans la table
-- La clause SET définit la nouvelle valeur pour la colonne score
-- La clause WHERE filtre les enregistrements pour ne modifier que ceux où name='Bob'
-- Cette requête permet de changer le score sans avoir à connaître l'id de l'utilisateur
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
