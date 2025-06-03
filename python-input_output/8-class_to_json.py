#!/usr/bin/python3
"""
Module contenant la fonction class_to_json qui retourne un dictionnaire
représentant un objet sérialisable en JSON.
"""


def class_to_json(obj):
    """
    Retourne la description du dictionnaire d'un objet pour sérialisation JSON.

    Args:
        obj: Instance d'une classe avec attributs sérialisables

    Returns:
        dict: Dictionnaire représentant l'objet
    """
    return obj.__dict__
