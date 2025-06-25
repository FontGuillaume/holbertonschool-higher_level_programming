-- Ce script crée une table appelée unique_id si elle n'existe pas déjà
-- La table contient deux colonnes: id (entier) et name (chaîne de caractères)
-- La colonne id a une valeur par défaut de 1 et possède la contrainte UNIQUE
-- Cette structure garantit que chaque valeur d'id sera unique dans la table
CREATE table IF NOT EXISTS unique_id (
    id INT default 1 UNIQUE,
    name VARCHAR(256)
);