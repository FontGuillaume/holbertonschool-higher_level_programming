#!/usr/bin/python3
"""
Module contenant la fonction pascal_triangle qui génère le triangle de Pascal.
"""


def pascal_triangle(n):
    """
    Génère le triangle de Pascal jusqu'à la n-ième ligne.

    Args:
        n (int): Nombre de lignes du triangle à générer

    Returns:
        list: Liste de listes représentant le triangle de Pascal
    """
    if n <= 0:
        return []

    result = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = result[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        result.append(row)

    return result
