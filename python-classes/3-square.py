#!/usr/bin/python3
"""
Module définissant une classe Square avec validation
de taille et calcul d'aire.
"""


class Square:
    """
    Classe représentant un carré.

    Cette classe définit un carré avec une taille validée et
    permet de calculer son aire.
    """

    def __init__(self, size=0):
        """
        Initialise une nouvelle instance de la classe Square.

        Args:
            size (int, optional): La taille du côté du carré. Défaut à 0.

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est négatif.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Attribut privé pour stocker la taille

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Returns:
            int: L'aire du carré (taille au carré).
        """
        return self.__size * self.__size
