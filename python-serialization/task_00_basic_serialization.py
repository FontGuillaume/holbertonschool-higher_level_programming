#!/usr/bin/env python3
"""
Module pour la sérialisation et désérialisation de données en format JSON.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise des données en JSON et les enregistre dans un fichier.

    Args:
        data: Les données à sérialiser (dict, list, str, int, etc.)
        filename (str): Nom du fichier où enregistrer les données
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Charge et désérialise des données JSON depuis un fichier.

    Args:
        filename (str): Nom du fichier contenant les données JSON

    Returns:
        Les données désérialisées (dict, list, str, int, etc.)
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
