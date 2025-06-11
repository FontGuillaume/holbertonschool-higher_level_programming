#!/usr/bin/python3
'''
Module implémentant un serveur HTTP RESTful simple.
'''
import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    '''
    Classe de gestionnaire HTTP personnalisée.
    '''

    def do_GET(self):
        '''
        Méthode qui traite les requêtes GET.
        '''
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            my_dict = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(my_dict).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header(
                "Content-type",
                "text/plain")  # Changé en text/plain
            self.end_headers()
            self.wfile.write(b'{"status":"OK"}')

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API "
                    "built with http.server"}
            self.wfile.write(json.dumps(info).encode())

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    '''
    Fonction qui démarre le serveur HTTP.
    '''
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Starting http server on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    '''
    Point d'entrée du script.
    '''
    run()
