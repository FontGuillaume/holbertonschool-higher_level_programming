#!/usr/bin/python3
"""
Module contenant la fonction say_my_name qui affiche le prénom et le nom
"""


def say_my_name(first_name, last_name=""):
    """
    Affiche "My name is <first_name> <last_name>".

    Args:
        first_name (str): Le prénom à afficher
        last_name (str, optional): Le nom à afficher. Par défaut "".

    Raises:
        TypeError: Si first_name n'est pas une chaîne de caractères
        TypeError: Si last_name n'est pas une chaîne de caractères
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))