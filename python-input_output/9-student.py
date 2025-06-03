#!/usr/bin/python3
"""
Module contenant la classe Student qui définit un étudiant.
"""


class Student:
    """Classe qui définit un étudiant."""

    def __init__(self, first_name, last_name, age):
        """
        Initialise un nouvel étudiant.

        Args:
            first_name (str): Prénom de l'étudiant
            last_name (str): Nom de famille de l'étudiant
            age (int): Âge de l'étudiant
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retourne un dictionnaire représentant l'étudiant.

        Returns:
            dict: Dictionnaire contenant les attributs de l'étudiant
        """
        return self.__dict__
