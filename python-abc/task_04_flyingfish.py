#!/usr/bin/env python3

class Fish:
    """
    Classe représentant un poisson avec ses comportements caractéristiques.
    """

    def swim(self):
        """
        Méthode qui représente la capacité du poisson à nager.
        Affiche un message indiquant que le poisson nage.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Méthode qui décrit l'habitat naturel du poisson.
        Affiche un message indiquant que le poisson vit dans l'eau.
        """
        print("The fish lives in water")


class Bird:
    """
    Classe représentant un oiseau avec ses comportements caractéristiques.
    """

    def fly(self):
        """
        Méthode qui représente la capacité de l'oiseau à voler.
        Affiche un message indiquant que l'oiseau vole.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Méthode qui décrit l'habitat naturel de l'oiseau.
        Affiche un message indiquant que l'oiseau vit dans le ciel.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Classe représentant un poisson volant qui hérite à la fois des
    caractéristiques d'un poisson et d'un oiseau.
    Exemple de multiple héritage en Python.
    """

    def fly(self):
        """
        Redéfinition de la méthode fly pour le poisson volant.
        Affiche un message spécifique au poisson volant en plein vol.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Redéfinition de la méthode swim pour le poisson volant.
        Affiche un message spécifique au poisson volant nageant.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Redéfinition de la méthode habitat pour le poisson volant.
        Affiche un message indiquant que le poisson volant vit à la fois
        dans l'eau et dans le ciel.
        """
        print("The flying fish lives both in water and the sky!")
