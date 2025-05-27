#!/usr/bin/env python3
'''
Ce module implémente un système de formes géométriques
avec des classes abstraites.
Il démontre le concept de "duck typing" en Python, où l'interface d'un objet
est définie par son comportement plutôt que par son héritage.

Le module contient:
- Une classe abstraite Shape qui définit l'interface
pour les formes géométriques
- Deux classes concrètes: Circle et Rectangle qui héritent de Shape
- Une fonction utilitaire shape_info qui utilise le duck typing
'''
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Classe abstraite qui définit l'interface
    pour toutes les formes géométriques.
    """
    @abstractmethod
    def area(self):
        """
        Méthode abstraite qui calcule l'aire de la forme.
        Doit être implémentée par toutes les sous-classes.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Méthode abstraite qui calcule le périmètre de la forme.
        Doit être implémentée par toutes les sous-classes.
        """
        pass


class Circle(Shape):
    """
    Classe représentant un cercle, qui
    hérite de la classe abstraite Shape.
    """

    def __init__(self, radius):
        """
        Initialise un cercle avec un rayon donné.

        Args:
            radius (float): Le rayon du cercle
        """
        self.radius = radius

    def area(self):
        """
        Calcule l'aire du cercle.

        Returns:
            float: L'aire du cercle (π * r²)
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calcule la circonférence du cercle.

        Returns:
            float: La circonférence du cercle (2 * π * r)
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Classe représentant un rectangle, qui
    hérite de la classe abstraite Shape.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec une
        largeur et une hauteur données.

        Args:
            width (float): La largeur du rectangle
            height (float): La hauteur du rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            float: L'aire du rectangle (largeur * hauteur)
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Returns:
            float: Le périmètre du rectangle (2 * (largeur + hauteur))
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Fonction qui affiche les informations d'une forme géométrique.

    Cette fonction utilise le duck typing, elle accepte tout objet ayant
    les méthodes area() et perimeter(), sans vérifier son type réel.

    Peu importe si l'objet est une instance de
    Shape ou non - si ça marche comme
    une forme (a les méthodes requises), alors c'est
    une forme pour cette fonction.

    Args:
        shape: Un objet qui implémente les méthodes area() et perimeter()
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

    if __name__ == "__main__":
        # Test des classes
        circle = Circle(radius=5)
        rectangle = Rectangle(width=4, height=7)

        shape_info(circle)
        shape_info(rectangle)
