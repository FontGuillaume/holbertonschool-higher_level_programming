-- Ce script SQL crée une table nommée 'first_table' si elle n'existe pas déjà
-- La clause IF NOT EXISTS évite de générer une erreur si la table existe déjà
-- La table contient deux colonnes:
--   - 'id' de type INT pour stocker des nombres entiers
--   - 'name' de type VARCHAR(256) pour stocker des chaînes de caractères jusqu'à 256 caractères
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
