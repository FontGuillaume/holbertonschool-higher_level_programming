#!/usr/bin/python3
"""
Module qui définit la classe MyList, une classe qui hérite de la classe list.
"""


class MyList(list):
    """
    Classe MyList qui hérite de la classe list.

    Cette classe étend les fonctionnalités de la classe list en ajoutant
    une méthode pour imprimer la liste triée.
    """

    def print_sorted(self):
        """
        Imprime la liste triée en ordre ascendant.

        Cette méthode ne modifie pas la liste originale,
        elle imprime simplement une version triée.
        """
        print(sorted(self))
