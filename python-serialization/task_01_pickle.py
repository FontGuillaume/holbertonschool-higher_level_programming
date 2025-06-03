#!/usr/bin/env python3
"""
Module pour la sérialisation et désérialisation d'objets avec pickle.
"""
import pickle


class CustomObject:
    """
    Classe représentant un objet personnalisé avec des fonctionnalités
    de sérialisation.
    """

    def __init__(self, name, age, is_student):
        """
        Initialise un nouvel objet CustomObject.

        Args:
            name (str): Nom de la personne
            age (int): Âge de la personne
            is_student (bool): Indique si la personne est étudiante
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Affiche les informations de l'objet.
        """
        print("Name {}".format(self.name))
        print("Age : {}".format(self.age))
        print("is student : {}".format(self.is_student))

    def serialize(self, filename):
        """
        Sérialise l'objet et le sauvegarde dans un fichier.

        Args:
            filename (str): Nom du fichier où enregistrer l'objet
        """
        with open(filename, "wb") as file:
            return pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Charge et désérialise un objet depuis un fichier.

        Args:
            filename (str): Nom du fichier contenant l'objet sérialisé

        Returns:
            CustomObject: L'objet désérialisé ou None en cas d'erreur
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
