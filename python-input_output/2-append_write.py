#!/usr/bin/python3
"""
Module contenant la fonction append_write qui ajoute une chaîne
de caractères à la fin d'un fichier texte.
"""


def append_write(filename="", text=""):
    """
    Ajoute une chaîne de caractères à la fin d'un fichier texte.

    Args:
        filename (str): Chemin du fichier où ajouter
        le texte. Par défaut, chaîne vide.
        text (str): Texte à ajouter dans le fichier. Par défaut, chaîne vide.

    Returns:
        int: Nombre de caractères ajoutés dans le fichier.
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
    return len(text)
