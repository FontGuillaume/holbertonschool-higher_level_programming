#!/usr/bin/python3
"""
Module qui définit la fonction inherits_from pour
vérifier si un objet hérite d'une classe spécifiée.
"""


def inherits_from(obj, a_class):
    """
    Vérifie si un objet est une instance d'une classe
    qui a hérité de la classe spécifiée,
    mais pas une instance directe de cette classe.

    Args:
        obj: L'objet à vérifier
        a_class: La classe à comparer

    Returns:
        True si l'objet hérite de la classe spécifiée sans
        être une instance directe, sinon False
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
