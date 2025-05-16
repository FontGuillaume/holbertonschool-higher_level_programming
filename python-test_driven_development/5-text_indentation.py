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
    skip_space = False  # Pour savoir si on doit ignorer les espaces

    while i < len(text):
        # Ignorer les espaces après les caractères spéciaux
        if skip_space and text[i] == ' ':
            i += 1
            continue

        skip_space = False

        # Imprimer le caractère courant
        print(text[i], end="")

        # Si c'est un caractère spécial, ajouter 2 nouvelles lignes
        if text[i] in special_chars:
            print("\n\n", end="")
            skip_space = True  # Commencer à ignorer les espaces

        i += 1
