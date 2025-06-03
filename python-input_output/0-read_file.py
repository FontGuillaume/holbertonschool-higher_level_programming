#!/usr/bin/python3
"""
Module contenant la fonction read_file qui lit un fichier texte
et imprime son contenu à la sortie standard.
"""


def read_file(filename=""):
    """
    Lit un fichier texte et imprime son contenu.

    Args:
        filename (str): Chemin du fichier à lire. Par défaut, chaîne vide.

    Returns:
        None: La fonction imprime le contenu mais ne retourne rien.
    """
    with open(filename, encoding="utf-8") as file:
        file = file.read()
        print(file, end="")
