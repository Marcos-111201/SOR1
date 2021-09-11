import http.server
import socketserver

PORT = 8080

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Servidor HTTP disponível na porta ", PORT)
    httpd.serve_forever()