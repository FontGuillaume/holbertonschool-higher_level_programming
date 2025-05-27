#!/usr/bin/python3
class CountedIterator:
    """
    Un itérateur qui garde une trace du nombre d'éléments parcourus.
    """

    def __init__(self, my_list):
        """
        Initialise l'itérateur avec une liste.

        Args:
            my_list: La liste à parcourir
        """
        self.my_list = my_list
        self.iterator = iter(my_list)
        self.index = 0

    def get_count(self):
        """
        Retourne le nombre d'éléments déjà parcourus.

        Returns:
            int: Le nombre d'éléments parcourus
        """
        return self.index

    def __next__(self):
        """
        Passe à l'élément suivant et incrémente le compteur.

        Returns:
            L'élément suivant dans l'itération

        Raises:
            StopIteration: Quand il n'y a plus d'éléments à parcourir
        """
        try:
            item = next(self.iterator)
            self.index += 1
            return item
        except StopIteration:
            raise StopIteration
