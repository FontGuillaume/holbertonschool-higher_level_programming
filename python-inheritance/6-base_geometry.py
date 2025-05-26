#!/usr/bin/python3
"""
Module qui définit la classe BaseGeometry, une
classe de base pour les formes géométriques.
"""


class BaseGeometry:
    """
    Classe de base pour les formes géométriques.

    Cette classe est conçue pour être une classe de
    base pour différentes
    formes géométriques et sera étendue par des classes filles.
    """

    def area(self):
        """
        Calcule l'aire de la forme géométrique.

        Cette méthode doit être implémentée par les classes filles.

        Raises:
            Exception: Cette méthode n'est pas implémentée
            dans la classe de base
        """
        raise Exception("area() is not implemented")
