#!/usr/bin/python3
"""
Module contenant la fonction to_json_string qui convertit un objet Python
en chaîne JSON.
"""
import json


def to_json_string(my_obj):
    """
    Retourne la représentation JSON d'un objet Python.

    Args:
        my_obj: L'objet Python à convertir en chaîne JSON.

    Returns:
        str: Chaîne de caractères au format JSON représentant l'objet.
    """
    return json.dumps(my_obj)
