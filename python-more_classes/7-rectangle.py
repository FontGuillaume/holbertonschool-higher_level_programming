#!/usr/bin/python3
"""
Module qui définit une classe Rectangle avec attributs, méthodes,
représentations en chaîne, compteur d'instances et symbole configurable
"""


class Rectangle:
    """
    Classe Rectangle qui définit un rectangle par sa largeur et sa hauteur.

    Attributes:
        width (int): La largeur du rectangle
        height (int): La hauteur du rectangle
        number_of_instances (int): Compteur du nombre d'instances créées
        print_symbol (any): Symbole utilisé pour la représentation en chaîne
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialisation d'une nouvelle instance de Rectangle.

        Args:
            width (int, optional): La largeur du rectangle. Par défaut 0.
            height (int, optional): La hauteur du rectangle. Par défaut 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        pour l'affichage, en utilisant le symbole défini dans print_symbol.

        Returns:
            str: Une représentation du rectangle avec le symbole configuré,
            ou une chaîne vide si la largeur ou la hauteur est 0
        """
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join([str(self.print_symbol) *
                          self.width for i in range(self.height)])

    def __repr__(self):
        """
        Définit la représentation en chaîne de caractères du rectangle
        qui peut être utilisée pour recréer une nouvelle instance.

        Returns:
            str: Une représentation de l'objet
            sous forme "Rectangle(width, height)"
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Méthode appelée lors de la suppression de l'instance.

        Décrémente le compteur d'instances et affiche un message d'adieu
        lorsqu'une instance de Rectangle est supprimée.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
