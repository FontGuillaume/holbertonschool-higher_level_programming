#!/usr/bin/python3
"""
Module qui définit la classe BaseGeometry, une
classe de base pour les formes géométriques.
"""


class BaseGeometry:
    """
    Classe de base pour les formes géométriques.

    Cette classe est conçue pour être une classe de base pour différentes
    formes géométriques et sera étendue par des classes filles.
    """

    def area(self):
        """
        Calcule l'aire de la forme géométrique.

        Cette méthode doit être implémentée par les classes filles.

        Raises:
            Exception: Cette méthode n'est pas
            implémentée dans la classe de base
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que la valeur est un entier positif.

        Args:
            name (str): Le nom de la valeur à valider
            value: La valeur à valider

        Raises:
            TypeError: Si value n'est pas un entier
            ValueError: Si value est inférieur ou égal à 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
