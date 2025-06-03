#!/usr/bin/env python3
"""
Module pour convertir des données CSV en format JSON.
"""
import csv
import json


def convert_csv_to_json(csv_filename, json_filename=None):
    """
    Convertit un fichier CSV en fichier JSON.

    Args:
        csv_filename (str): Nom du fichier CSV source
        json_filename (str, optional): Nom du fichier JSON de destination.
                                       Par défaut: même nom que source + .json

    Returns:
        bool: True si conversion réussie, False sinon
    """
    if json_filename is None:
        json_filename = csv_filename.split('.')[0] + '.json'

    try:
        """
        Lecture du fichier CSV et conversion en liste de dictionnaires
        """
        with open(csv_filename, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

        """
        Écriture des données au format JSON avec indentation pour lisibilité
        """
        with open(json_filename, "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True
    except Exception:
        return False
    except FileNotFoundError:
        return False
