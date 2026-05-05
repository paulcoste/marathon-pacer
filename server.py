#!/usr/bin/env python3
"""
Serveur local pour tester la PWA marathon-pacer.
Lance avec : python server.py
Puis ouvre http://localhost:8080 dans Chrome/Safari
"""
import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Headers nécessaires pour PWA
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Service-Worker-Allowed', '/')
        super().end_headers()

    def log_message(self, format, *args):
        print(f"  {args[0]} {args[1]}")

print(f"🏃 Pacer — serveur local")
print(f"   http://localhost:{PORT}")
print(f"   Ctrl+C pour arrêter\n")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
