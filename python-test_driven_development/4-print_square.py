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
        ValueError: Si size est inférieur à 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
