#!/usr/bin/python3
class VerboseList(list):
    """
    Une classe qui étend la classe list native pour fournir des retours
    verbeux lors des opérations courantes.
    """

    def append(self, item):
        """
        Ajoute un élément à la fin de la liste et affiche un message.

        Args:
            item: L'élément à ajouter à la liste
        """
        super().append(item)
        print("Added [{}] to the list".format(item))

    def extend(self, iterable):
        """
        Étend la liste avec les éléments d'un itérable et affiche un message.

        Args:
            iterable: Collection d'éléments à ajouter à la liste
        """
        super().extend(iterable)
        print("Extended the list with [{}] items".format(len(iterable)))

    def remove(self, item):
        """
        Supprime la première occurrence d'un élément et affiche un message.

        Args:
            item: L'élément à supprimer de la liste
        """
        super().remove(item)  # Ce code était manquant dans l'original
        print("Remove [{}] from the list".format(item))

    def pop(self, index=-1):
        """
        Supprime et retourne l'élément à l'index
        spécifié et affiche un message.

        Args:
            index: L'index de l'élément à supprimer (par défaut: -1)

        Returns:
            L'élément supprimé
        """
        item = super().pop(index)
        print("Popped [{}] from the list".format(item))
        return item
