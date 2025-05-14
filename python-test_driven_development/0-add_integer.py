#!/usr/bin/python3
"""
Module qui contient la fonction add_integer pour additionner deux entiers
"""


def add_integer(a, b=98):
    """
    Additionne deux entiers.

    Args:
        a (int, float): Premier nombre
        b (int, float, optional): Deuxième nombre. Par défaut 98.

    Returns:
        int: La somme de a et b en tant qu'entier

    Raises:
        TypeError: Si a ou b n'est pas un entier ou un flottant
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
