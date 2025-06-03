#!/usr/bin/python3
"""
Module contenant la fonction load_from_json_file qui crée un objet Python
à partir d'un fichier JSON.
"""
import json


def load_from_json_file(filename):
    """
    Crée un objet Python à partir d'un fichier JSON.

    Args:
        filename (str): Nom du fichier JSON à charger.

    Returns:
        object: L'objet Python créé à partir du fichier JSON.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
