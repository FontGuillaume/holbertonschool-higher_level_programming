#!/usr/bin/env python3
"""
Module pour la sérialisation et désérialisation de données en format XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire en XML et l'enregistre dans un fichier.

    Args:
        dictionary (dict): Dictionnaire à sérialiser
        filename (str): Nom du fichier où enregistrer les données XML
    """
    # Création de l'élément racine
    root = ET.Element("data")
    # Ajout de chaque paire clé-valeur comme élément enfant
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = value
    # Création de l'arbre XML et écriture dans le fichier
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Charge et désérialise des données XML depuis un fichier.

    Args:
        filename (str): Nom du fichier contenant les données XML

    Returns:
        dict: Dictionnaire contenant les données désérialisées
    """
    # Analyse du fichier XML et récupération de la racine
    tree = ET.parse(filename)
    root = tree.getroot()
    # Création du dictionnaire résultat
    result = {}
    # Parcours des éléments enfants pour extraire les paires clé-valeur
    for child in root:
        key = child.tag
        value = child.text
        result[key] = value
    return result
