#!/usr/bin/python3
"""
Module qui définit une classe Rectangle avec attributs, méthodes,
représentations en chaîne et message de suppression
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

    def area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            int: L'aire du rectangle (largeur × hauteur)
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Returns:
            int: Le périmètre du rectangle (2 × (largeur + hauteur))
            ou 0 si la largeur ou la hauteur est nulle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        """
        Définit la représentation en chaîne de caractères du rectangle
        pour l'affichage.

        Returns:
            str: Une représentation du rectangle avec des caractères '#',
            ou une chaîne vide si la largeur ou la hauteur est 0
        """
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join(["#" * self.width for i in range(self.height)])

    def __repr__(self):
        """
        Définit la représentation en chaîne de caractères du rectangle
        qui peut être utilisée pour recréer une nouvelle instance.

        Returns:
            str: Une représentation de l'objet sous forme "Rectangle(width, height)"
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Méthode appelée lors de la suppression de l'instance.

        Affiche un message d'adieu lorsqu'une instance de Rectangle
        est supprimée.
        """
        print("Bye rectangle...")
