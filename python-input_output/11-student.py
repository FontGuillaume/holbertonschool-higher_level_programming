#!/usr/bin/python3
"""
Module contenant la classe Student qui définit un étudiant.
"""


class Student:
    """Classe qui définit un étudiant."""

    def __init__(self, first_name, last_name, age):
        """Initialise un nouvel étudiant."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retourne un dictionnaire représentant l'étudiant."""
        if attrs is None:
            return self.__dict__

        return {attr: getattr(self, attr) for attr in attrs
                if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Remplace tous les attributs de l'instance Student.

        Args:
            json (dict): Dictionnaire contenant les attributs à remplacer
        """
        for key in json:
            setattr(self, key, json[key])
