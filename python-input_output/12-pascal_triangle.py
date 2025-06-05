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

    triangle = []

    for i in range(n):
        row = [1]

        if i > 1:
            for j in range(1, i):
                val = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(val)

        if i > 0:
            row.append(1)

        triangle.append(row)

    return triangle