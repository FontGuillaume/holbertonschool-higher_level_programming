-- Ce script crée une table appelée id_not_null si elle n'existe pas déjà
-- La table contient deux colonnes: id (entier) et name (chaîne de caractères)
-- La colonne id a une valeur par défaut de 1, ce qui garantit qu'elle ne sera jamais NULL
-- Cette structure permet d'avoir un identifiant pour chaque enregistrement même si aucune valeur n'est spécifiée
CREATE table IF NOT EXISTS id_not_null (
    id INT default 1,
    name VARCHAR(256)
);