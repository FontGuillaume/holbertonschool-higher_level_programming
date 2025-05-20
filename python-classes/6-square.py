#!/usr/bin/python3
class Square:
    """
    Classe représentant un carré avec une taille et une position.
    Utilise l'encapsulation pour protéger les attributs privés.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialisation d'un carré.

        Args:
            size (int): Taille du côté du carré (par défaut 0)
            position (tuple): Position du carré (par défaut (0,0))

        Note: La validation de position n'est pas effectuée ici,
        ce qui est un problème
        car on stocke position avant de vérifier sa validité dans le setter.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Attribut privé pour la taille
        self.__position = position  # Attribut privé pour la position

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Returns:
            int: L'aire du carré (taille au carré)
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter pour l'attribut size.
        Cette propriété permet d'accéder à l'attribut privé __size.

        Returns:
            int: La taille du carré
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Setter pour l'attribut size.
        Valide que la taille est un entier positif avant de l'assigner.

        Args:
            size (int): Nouvelle taille du carré

        Raises:
            TypeError: Si size n'est pas un entier
            ValueError: Si size est négatif
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """
        Affiche le carré avec des caractères '#'.
        Prend en compte la position pour l'affichage:
        - position[1] lignes vides avant le carré
        - position[0] espaces avant chaque ligne du carré

        Si size est 0, affiche seulement une ligne vide.
        """
        if self.__size == 0:
            print()  # Si taille 0, juste une ligne vide
            return

        # Affiche les lignes vides selon la position verticale
        for _ in range(self.__position[1]):
            print()

        # Affiche les lignes du carré
        for _ in range(self.__size):
            # Pour chaque ligne: espaces horizontaux puis caractères '#'
            print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """
        Getter pour l'attribut position.
        Cette propriété permet d'accéder à l'attribut privé __position.

        Returns:
            tuple: La position du carré (x, y)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter pour l'attribut position.
        Valide que la position est un tuple de 2 entiers positifs.

        Args:
            value (tuple): Nouvelle position du carré

        Raises:
            TypeError: Si value n'est pas un tuple de 2 entiers positifs
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
