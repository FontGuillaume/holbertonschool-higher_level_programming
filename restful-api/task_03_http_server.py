#!/usr/bin/python3
'''
Module implémentant un serveur HTTP RESTful simple.
Fournit plusieurs endpoints pour démontrer les bases d'une API RESTful.
'''
import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class new_class(BaseHTTPRequestHandler):
    '''
    Classe de gestionnaire HTTP personnalisée qui étend BaseHTTPRequestHandler.
    Gère les requêtes GET pour différents endpoints de l'API.
    '''

    def do_GET(self):
        '''
        Méthode qui traite toutes les requêtes GET reçues par le serveur.
        Implémente plusieurs endpoints et renvoie des réponses appropriées.
        '''
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            my_dict = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            json_my_dict = json.dumps(my_dict)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_my_dict.encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "OK"}).encode())

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            json_info = json.dumps({"version": "1.0", "description": "A "
                                    "simple API built "
                                    "with http.server"})
            self.wfile.write(json_info.encode())

        else:
            self.send_response(404)
            self.send_header("Content-Type", 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(
                {"error": "Endpoint not found"}).encode())


def run(server_class=HTTPServer, handler_class=new_class):
    '''
    Fonction qui initialise et démarre le serveur HTTP.
    Params:
        server_class: Classe de serveur à utiliser (par défaut HTTPServer)
        handler_class: Classe de gestionnaire à utiliser (par défaut new_class)
    '''
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Starting http server on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    '''
    Point d'entrée du script quand il est exécuté directement.
    Démarre le serveur HTTP.
    '''
    run()
