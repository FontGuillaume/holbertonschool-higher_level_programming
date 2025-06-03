#!/usr/bin/python3
"""
Module contenant la fonction save_to_json_file qui écrit un objet Python
dans un fichier au format JSON.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Écrit un objet Python dans un fichier en utilisant sa représentation JSON.

    Args:
        my_obj: L'objet Python à sérialiser et sauvegarder.
        filename (str): Nom du fichier où sauvegarder l'objet.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
