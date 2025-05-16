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

    # Caractères spéciaux après lesquels il faut ajouter 2 nouvelles lignes
    special_chars = ['.', '?', ':']

    i = 0
    while i < len(text):
        # Imprimer le caractère courant
        print(text[i], end="")

        # Si c'est un caractère spécial, ajouter 2 nouvelles lignes
        if text[i] in special_chars:
            print("\n\n", end="")

            # Ignorer les espaces après le caractère spécial
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1
