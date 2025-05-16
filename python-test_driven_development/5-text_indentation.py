#!/usr/bin/python3
"""
Module contenant la fonction text_indentation pour formater du texte
"""


def text_indentation(text):
    """
    Imprime un texte avec 2 nouvelles lignes après chaque '.', '?' et ':'.

    Args:
        text (str): Le texte à formater et imprimer

    Raises:
        TypeError: Si text n'est pas une chaîne de caractères
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remplacer les caractères spéciaux par le caractère suivi de 2 nouvelles
    # lignes
    result = text
    for char in ['.', '?', ':']:
        result = result.replace(char, char + "\n\n")

    # Traiter chaque ligne pour supprimer les espaces en début et fin
    lines = result.split("\n")
    for i, line in enumerate(lines):
        print(line.strip() if i < len(lines) -
              1 or line.strip() else "", end="")
        if i < len(lines) - 1:
            print()
