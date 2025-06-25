-- Ce script crée une table appelée force_name si elle n'existe pas déjà
-- La table contient deux colonnes: id (entier) et name (chaîne de caractères)
-- La colonne name est définie avec la contrainte NOT NULL, ce qui oblige à avoir une valeur
-- Cette structure garantit que chaque enregistrement dans la table aura toujours un nom
CREATE table IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);