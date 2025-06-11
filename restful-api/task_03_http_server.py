#!/usr/bin/python3
'''
Module implémentant un serveur HTTP RESTful simple.
'''
import json
import sys
import os
import signal
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    '''
    Classe de gestionnaire HTTP personnalisée.
    '''
    protocol_version = 'HTTP/1.1'

    def do_GET(self):
        '''
        Méthode qui traite les requêtes GET.
        '''
        path = self.path.split('?')[0]  # Ignore query parameters

        if path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))

        elif path == "/data":
            my_dict = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(my_dict).encode('utf-8'))

        elif path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status_json = json.dumps({"status": "OK"})
            self.wfile.write(status_json.encode('utf-8'))

        elif path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode('utf-8'))


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    '''
    Fonction qui démarre le serveur HTTP.
    '''
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Starting http server on port 8000...")

    # Handle Ctrl+C gracefully
    signal.signal(signal.SIGINT, lambda s, f: (
        print("\nShutting down..."), sys.exit(0)))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        httpd.server_close()


if __name__ == "__main__":
    '''
    Point d'entrée du script.
    '''
    run()
