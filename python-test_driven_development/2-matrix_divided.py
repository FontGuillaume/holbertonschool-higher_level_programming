#!/usr/bin/python3
"""
Module contenant la fonction matrix_divided qui divise
les éléments d'une matrice
"""


def matrix_divided(matrix, div):
    """
    Divise tous les éléments d'une matrice par un nombre.

    Args:
        matrix (list): Une liste de listes de nombres (int ou float)
        div (int, float): Le diviseur

    Returns:
        list: Une nouvelle matrice avec tous les éléments divisés par div
              et arrondis à 2 décimales

    Raises:
        TypeError: Si matrix n'est pas une liste de listes de nombres
        TypeError: Si les lignes de la matrice ne sont pas de même taille
        TypeError: Si div n'est pas un nombre
        ZeroDivisionError: Si div est égal à 0
    """
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Vérifier que chaque ligne est une liste de nombres
    row_size = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats")

    # Vérifier div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Créer une nouvelle matrice avec les éléments divisés
    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix
