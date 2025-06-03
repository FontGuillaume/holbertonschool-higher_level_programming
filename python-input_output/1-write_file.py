#!/usr/bin/python3
"""
Module contenant la fonction write_file qui écrit une chaîne
de caractères dans un fichier texte.
"""


def write_file(filename="", text=""):
    """
    Écrit une chaîne de caractères dans un fichier texte.

    Args:
        filename (str): Chemin du fichier où écrire. Par défaut, chaîne vide.
        text (str): Texte à écrire dans le fichier. Par défaut, chaîne vide.

    Returns:
        int: Nombre de caractères écrits dans le fichier.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    return len(text)
