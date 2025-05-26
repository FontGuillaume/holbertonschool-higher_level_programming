#!/usr/bin/python3
"""
Module qui définit la classe Square, héritant de Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Classe Square qui hérite de Rectangle.

    Cette classe représente un carré, qui est un cas particulier
    de rectangle où la largeur et la hauteur sont identiques.
    """

    def __init__(self, size):
        """
        Initialise une nouvelle instance de Square.

        Args:
            size (int): La taille du carré, doit être un entier positif

        Raises:
            TypeError: Si size n'est pas un entier
            ValueError: Si size est inférieur ou égal à 0
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calcule l'aire du carré.

        Returns:
            int: L'aire du carré (taille au carré)
        """
        return self.__size ** 2

    def __str__(self):
        """
        Retourne une représentation textuelle du carré.

        Returns:
            str: Une chaîne de caractères au
            format "[Rectangle] <taille>/<taille>"
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
