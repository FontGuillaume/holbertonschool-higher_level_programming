-- Ce script crée un utilisateur MySQL avec tous les privilèges
-- L'utilisateur 'user_0d_1' est créé s'il n'existe pas déjà
-- Le mot de passe de cet utilisateur est défini comme 'user_0d_1_pwd'
-- Tous les privilèges sont accordés à cet utilisateur sur toutes les bases de données
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
