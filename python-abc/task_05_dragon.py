#!/usr/bin/env python3

class SwimMixin:
    """
    Mixin qui fournit la capacité de nager.
    Peut être utilisé avec n'importe
    quelle classe nécessitant cette fonctionnalité.
    """

    def swim(self):
        """
        Méthode qui représente l'action de nager.
        Affiche un message indiquant que la créature nage.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin qui fournit la capacité de voler.
    Peut être utilisé avec n'importe
    quelle classe nécessitant cette fonctionnalité.
    """

    def fly(self):
        """
        Méthode qui représente l'action de voler.
        Affiche un message indiquant que la créature vole.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Classe Dragon qui hérite des capacités de nager et de voler
    grâce aux mixins SwimMixin et FlyMixin.
    Démontre l'utilisation des mixins pour la composition de comportements.
    """

    def roar(self):
        """
        Méthode spécifique au dragon qui représente son rugissement.
        Affiche un message indiquant que le dragon rugit.
        """
        print("The dragon roars!")


# Création d'une instance de Dragon
draco = Dragon()
