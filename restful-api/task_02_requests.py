#!/usr/bin/python3
'''
Module pour récupérer des données depuis une API REST externe.
Permet de récupérer des posts et de les afficher ou les sauvegarder.
'''
import requests
import csv


def fetch_and_print_posts():
    '''
    Fonction qui récupère des posts depuis JSONPlaceholder et les affiche.
    Affiche le statut de la requête et le titre de chaque post.
    '''
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    print("Status code {}".format(r.status_code))

    if r.status_code == 200:
        data = r.json()
        for post in data:
            print("{}".format(post['title']))


def fetch_and_save_posts():
    '''
    Fonction qui récupère des posts depuis JSONPlaceholder
    et les sauvegarde dans un fichier CSV.
    Extrait l'id, le titre et le corps de chaque
    post et les enregistre dans posts.csv.
    '''
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)

    if r.status_code == 200:
        posts = []
        data = r.json()
        posts.append({"id": post["id"], "title": post["title"], "body":
                      post["body"]} for post in data)

        with open("posts.csv", "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)


if __name__ == "__main__":
    print("Fetching and printing posts:")
    fetch_and_print_posts()

    print("\nFetching and saving posts to CSV:")
    fetch_and_save_posts()
