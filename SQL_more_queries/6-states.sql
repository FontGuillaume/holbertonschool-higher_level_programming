-- Ce script crée une base de données et une table pour stocker des états
-- La base de données hbtn_0d_usa est créée si elle n'existe pas déjà
-- La table states contient un id unique auto-incrémenté qui sert de clé primaire
-- Chaque état a également un nom qui ne peut pas être NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE table IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);