#!/usr/bin/python3
"""
Module définissant une classe Square avec validation de la taille.
"""


class Square:
    """
    Classe représentant un carré.

    Cette classe définit un carré avec une taille validée.
    La taille est stockée comme un attribut privé et
    doit être un entier positif.
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

    @property
    def get_size(self):
        """
        Accède à la taille du carré.

        Returns:
            int: La taille actuelle du carré.

        Note:
            Cette propriété devrait s'appeler
            simplement 'size' pour suivre
            les conventions de nommage Python pour les propriétés.
        """
        return self.__size

    @property
    def setsize(self, size):
        """
        Définit la taille du carré.

        Args:
            size (int): La nouvelle taille du carré.

        Note:
            Cette implémentation est incorrecte car:
            1. Elle devrait être un décorateur @get_size.setter
            et non @property
            2. Le nom devrait correspondre à la propriété
            getter ('size' idéalement)
            3. Il manque la validation du type et de la valeur
        """
        self.__size = size
