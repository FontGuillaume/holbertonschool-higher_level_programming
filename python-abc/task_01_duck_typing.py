#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


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

    Args:
        shape: Un objet qui implémente les méthodes area() et perimeter()
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
