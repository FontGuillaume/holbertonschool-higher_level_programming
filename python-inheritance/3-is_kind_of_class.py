#!/usr/bin/python3
"""
Module qui définit la fonction is_kind_of_class
pour vérifier l'héritage d'un objet.
"""


def is_kind_of_class(obj, a_class):
    """
    Vérifie si un objet est une instance ou une instance
    d'une classe qui a hérité de la classe spécifiée.

    Args:
        obj: L'objet à vérifier
        a_class: La classe à comparer

    Returns:
        True si l'objet est une instance ou
        hérite de la classe spécifiée, sinon False
    """
    return isinstance(obj, a_class)
