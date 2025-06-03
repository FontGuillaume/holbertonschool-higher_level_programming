#!/usr/bin/python3
"""
Script qui ajoute tous les arguments à une liste Python,
puis les sauvegarde dans un fichier JSON.
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Tente de charger la liste depuis le fichier JSON
try:
    my_list = load_from_json_file("add_item.json")
except (FileNotFoundError, ValueError):
    # Crée une liste vide si le fichier n'existe pas ou n'est pas valide
    my_list = []

# Ajoute tous les arguments de la ligne de commande à la liste
my_list.extend(sys.argv[1:])

# Sauvegarde la liste mise à jour dans le fichier JSON
save_to_json_file(my_list, "add_item.json")
