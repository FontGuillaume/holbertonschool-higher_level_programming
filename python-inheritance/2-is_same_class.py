#!/usr/bin/python3
"""
Module qui définit la fonction is_same_class
pour vérifier le type exact d'un objet.
"""


def is_same_class(obj, a_class):
    """
    Vérifie si un objet est exactement une instance de la classe spécifiée.

    Args:
        obj: L'objet à vérifier
        a_class: La classe à comparer

    Returns:
        True si l'objet est exactement une
        instance de la classe spécifiée, sinon False
    """
    return type(obj) is a_class
