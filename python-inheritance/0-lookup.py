#!/usr/bin/python3
"""
Module qui définit la fonction lookup pour
retourner les attributs et méthodes d'un objet.
"""


def lookup(obj):
    """
    Retourne la liste des attributs et méthodes disponibles d'un objet.

    Args:
        obj: L'objet à examiner

    Returns:
        Une liste contenant les noms des attributs et méthodes de l'objet
    """
    return dir(obj)
