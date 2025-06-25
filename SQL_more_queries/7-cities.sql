-- Ce script crée une base de données et une table pour stocker des villes
-- La base de données hbtn_0d_usa est créée si elle n'existe pas déjà
-- La table cities contient un id unique auto-incrémenté qui sert de clé primaire
-- Chaque ville a un nom et est liée à un état via une clé étrangère state_id
-- La clé étrangère assure l'intégrité référentielle avec la table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE table IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);