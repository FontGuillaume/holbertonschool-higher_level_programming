#!/usr/bin/python3
"""
Module définissant une classe Square avec accès et
modification contrôlés de la taille.
"""


class Square:
    """
    Classe représentant un carré.

    Cette classe définit un carré avec une taille validée,
    permet de calculer son aire
    et utilise des propriétés pour accéder et modifier
    la taille de manière contrôlée.
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
        self.__size = size

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Returns:
            int: L'aire du carré (taille au carré).
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter pour récupérer la taille du carré.

        Cette propriété permet d'accéder à l'attribut privé __size.

        Returns:
            int: La taille actuelle du carré.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Setter pour modifier la taille du carré avec validation.

        Args:
            size (int): La nouvelle taille du carré.

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est négatif.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
