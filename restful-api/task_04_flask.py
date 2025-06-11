#!/usr/bin/python3
"""
Module pour créer une API RESTfull avec Flask
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire pour stocker les utilisateurs (vide au début)
users = {}

# Routes a définir ici


@app.route("/")
def home():
    """
    Route racine qui affiche un message de bienvenue
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """
    Renvoie la liste des noms d'utilisateurs stockés.
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """
    Renvoie le statut de l'API.

    Returns:
        str: Un message 'OK' indiquant que l'API fonctionne correctement.
    """
    return "OK"


@app.route("/users/<username>")
def get_username(username):
    """
    Récupère les informations d'un utilisateur spécifique.

    Args:
        username (str): Le nom d'utilisateur à rechercher.

    Returns:
        Response: Les données de l'utilisateur au format JSON si trouvé,
                 ou un message d'erreur avec code 404 si non trouvé.
    """
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Ajoute un nouvel utilisateur à partir des données JSON reçues.

    La requête doit contenir au minimum le champ 'username'.

    Returns:
        Response: Un message de confirmation avec les données de l'utilisateur
                 et code 201 si ajouté avec succès,
                 ou un message d'erreur avec code 400 si username manquant.
    """
    data = request.get_json()
    if "username" in data:
        users[data["username"]] = data
        return jsonify({"message": "User added", "user": data}), 201
    return jsonify({"error": "Username is required"}), 400


if __name__ == "__main__":
    app.run()
