-- Ce script SQL crée une table nommée 'second_table' si elle n'existe pas déjà
-- La table contient trois colonnes: id (INT), name (VARCHAR) et score (INT)
-- Puis le script insère plusieurs enregistrements dans cette table
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- La commande INSERT INTO avec VALUES multiples permet d'ajouter plusieurs lignes en une seule requête
-- Chaque parenthèse représente un nouvel enregistrement avec ses valeurs dans l'ordre des colonnes spécifiées
-- Cette méthode est plus efficace que d'utiliser plusieurs requêtes INSERT séparées
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
