#!/usr/bin/python3
"""
Module définissant une classe Square avec un attribut de taille privé.
"""


class Square:
    """
    Classe représentant un carré.

    Cette classe définit un carré par sa taille.
    La taille est stockée comme un attribut privé.
    """

    def __init__(self, size):
        """
        Initialise une nouvelle instance de la classe Square.

        Args:
            size: La taille du côté du carré
                 La valeur n'est pas validée et peut être
                 de n'importe quel type

        Note:
            La taille est stockée dans un attribut privé __size,
            ce qui la rend inaccessible directement depuis
            l'extérieur de la classe.
        """
        self.__size = size  # Attribut privé identifié par le double underscore
