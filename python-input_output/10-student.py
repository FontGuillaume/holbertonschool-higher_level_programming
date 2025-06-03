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

    def to_json(self, attrs=None):
        """
        Retourne un dictionnaire représentant l'étudiant.

        Args:
            attrs (list, optional): Liste des attributs à récupérer

        Returns:
            dict: Dictionnaire contenant les attributs demandés
        """
        if attrs is None:
            return self.__dict__

        return {attr: getattr(self, attr) for attr in attrs
                if hasattr(self, attr)}
