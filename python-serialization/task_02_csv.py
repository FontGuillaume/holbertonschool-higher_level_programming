#!/usr/bin/env python3
"""
Module pour convertir des données CSV en format JSON.
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Convertit un fichier CSV en fichier JSON.

    Args:
        filename (str): Nom du fichier CSV à convertir

    Returns:
        bool: True si la conversion a réussi, False sinon
    """
    try:
        with open(filename, "r", encoding="utf-8") as csvfile:
            READER = csv.DictReader(csvfile)
        data = list(csv.DictReader(csvfile))
        with open(data.json, "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile)
        return True
    except Exception:
        return False
    except FileNotFoundError:
        return False
