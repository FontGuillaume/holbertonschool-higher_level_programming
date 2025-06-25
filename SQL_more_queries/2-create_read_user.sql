-- Ce script crée une base de données et un utilisateur avec des privilèges de lecture uniquement
-- La base de données 'hbtn_0d_2' est créée si elle n'existe pas déjà
-- L'utilisateur 'user_0d_2' est créé s'il n'existe pas déjà avec le mot de passe 'user_0d_2_pwd'
-- Des privilèges SELECT (lecture seule) sont accordés à cet utilisateur sur la base de données hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';