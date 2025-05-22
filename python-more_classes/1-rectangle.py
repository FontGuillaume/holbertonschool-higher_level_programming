#!/usr/bin/python3
"""
Module qui définit une classe Rectangle avec des attributs largeur et hauteur
"""


class Rectangle:
    """
    Classe Rectangle qui définit un rectangle par sa largeur et sa hauteur.

    Attributes:
        width (int): La largeur du rectangle
        height (int): La hauteur du rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialisation d'une nouvelle instance de Rectangle.

        Args:
            width (int, optional): La largeur du rectangle. Par défaut 0.
            height (int, optional): La hauteur du rectangle. Par défaut 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter pour l'attribut width.

        Returns:
            int: La largeur du rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter pour l'attribut width.

        Args:
            value (int): La nouvelle largeur du rectangle

        Raises:
            TypeError: Si value n'est pas un entier
            ValueError: Si value est négatif
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter pour l'attribut height.

        Returns:
            int: La hauteur du rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter pour l'attribut height.

        Args:
            value (int): La nouvelle hauteur du rectangle

        Raises:
            TypeError: Si value n'est pas un entier
            ValueError: Si value est négatif
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
