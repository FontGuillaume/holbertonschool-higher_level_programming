#!/usr/bin/python3
"""
Module contenant la fonction from_json_string qui convertit une chaîne JSON
en objet Python.
"""
import json


def from_json_string(my_str):
    """
    Retourne un objet Python représenté par une chaîne de caractères JSON.

    Args:
        my_str (str): Chaîne de caractères au format JSON à convertir.

    Returns:
        object: Objet Python correspondant à la représentation JSON.
    """
    return json.loads(my_str)
