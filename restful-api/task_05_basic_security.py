#!/usr/bin/python3
"""
Module pour implémenter l'authentification et la sécurité dans une API Flask.
Utilise deux méthodes d'authentification : basique et JWT.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from flask_jwt_extended import JWTManager, create_access_token

# Initialisation de l'application Flask
app = Flask(__name__)
# Définition de la clé secrète pour signer les tokens JWT
app.config['JWT_SECRET_KEY'] = 'ma-cle-secrete'
# Initialisation du gestionnaire JWT
jwt = JWTManager(app)
# Initialisation de l'authentification basique
auth = HTTPBasicAuth()

# Dictionnaire des utilisateurs avec leurs mots de passe hachés et rôles
users = {
    "user1": {/
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"},
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"}}


@auth.verify_password
def verify_password(username, password):
    """
    Vérifie les identifiants pour l'authentification basique.

    Args:
        username: Nom d'utilisateur fourni dans la requête
        password: Mot de passe fourni dans la requête

    Returns:
        L'objet utilisateur si authentification réussie, None sinon
    """
    if username in users and check_password_hash(
            users[username]["password"], password):
        return users[username]
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Route protégée par authentification basique.

    Returns:
        Message de confirmation si l'authentification réussit
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """
    Route pour obtenir un token JWT via identifiants.

    Returns:
        Token JWT si authentification réussie
        Message d'erreur avec code 400/401 sinon
    """
    data = request.get_json()

    # Vérification de la présence des champs obligatoires
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data['username']
    password = data['password']

    # Vérification des identifiants
    if username in users and check_password_hash(
            users[username]["password"], password):
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token})

    return jsonify({"error": "Invalid username or password"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    Route protégée par authentification JWT.

    Returns:
        Message de confirmation si le token JWT est valide
    """
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    Route réservée aux administrateurs (protection par rôle).

    Returns:
        Message de confirmation si l'utilisateur est admin
        Message d'erreur avec code 403 sinon
    """
    current_user = get_jwt_identity()

    # Vérification du rôle admin
    if current_user not in users or users[current_user]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Gère les erreurs de token manquant."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Gère les erreurs de token invalide."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Gère les erreurs de token expiré."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Gère les erreurs de token révoqué."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Gère les erreurs de token non-frais."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    """Point d'entrée pour l'exécution de l'application."""
    app.run()
