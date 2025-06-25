-- Ce script affiche les privilèges des utilisateurs sur le serveur MySQL
-- Il liste les permissions accordées aux utilisateurs user_0d_1 et user_0d_2
-- Ces informations sont utiles pour vérifier les niveaux d'accès des utilisateurs
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
