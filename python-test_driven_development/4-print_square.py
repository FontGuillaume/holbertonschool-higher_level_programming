#!/usr/bin/python3
"""
Module contenant la fonction print_square pour imprimer un carré
"""


def print_square(size):
    """
    Imprime un carré de côté 'size' avec le caractère #.

    Args:
        size (int): La taille du côté du carré

    Raises:
        TypeError: Si size n'est pas un entier
        TypeError: Si size est un float négatif
        ValueError: Si size est inférieur à 0
    """
    # Vérification pour les floats négatifs (condition spécifique selon
    # l'énoncé)
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # Vérification générale du type
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Vérification pour les entiers négatifs
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
