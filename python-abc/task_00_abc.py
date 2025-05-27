#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Classe abstraite Animal qui définit l'interface pour tous les animaux.
    Cette classe ne peut pas être instanciée directement.
    """
    @abstractmethod
    def sound(self):
        """
        Méthode abstraite qui doit être
        implémentée par toutes les sous-classes.
        Cette méthode doit retourner le son caractéristique de l'animal.
        """
        pass


class Dog(Animal):
    """
    Classe représentant un chien, qui hérite de la classe abstraite Animal.
    """

    def sound(self):
        """
        Implémentation de la méthode sound pour un chien.
        Retourne le son caractéristique d'un chien.
        """
        return "Bark"


class Cat(Animal):
    """
    Classe représentant un chat, qui hérite de la classe abstraite Animal.
    """

    def sound(self):
        """
        Implémentation de la méthode sound pour un chat.
        Retourne le son caractéristique d'un chat.
        """
        return "Meow"
