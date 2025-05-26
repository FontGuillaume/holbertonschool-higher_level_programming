#!/usr/bin/python3
"""
Module qui définit la classe Rectangle, héritant de BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe Rectangle qui hérite de BaseGeometry.

    Cette classe représente un rectangle avec une largeur et une hauteur,
    et implémente les méthodes area et __str__.
    """

    def __init__(self, width, height):
        """
        Initialise une nouvelle instance de Rectangle.

        Args:
            width (int): La largeur du rectangle, doit être un entier positif
            height (int): La hauteur du rectangle, doit être un entier positif

        Raises:
            TypeError: Si width ou height n'est pas un entier
            ValueError: Si width ou height est inférieur ou égal à 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            int: L'aire du rectangle (largeur × hauteur)
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Retourne une représentation textuelle du rectangle.

        Returns:
            str: Une chaîne de caractères au
            format "[Rectangle] <largeur> / <hauteur>"
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
