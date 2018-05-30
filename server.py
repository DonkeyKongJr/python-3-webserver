from http.server import BaseHTTPRequestHandler,HTTPServer
from io import BytesIO
import re

enpoint_data_base_url = '/api/v1/data'
PORT = 5555

print("Python webserver starting at PORT: " + str(PORT))

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'This is a simple HTTP Server with Get and Post endpoints.')

    def do_POST(self):        
        if None != re.search(enpoint_data_base_url + '/*', self.path):
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            self.send_response(200)
            self.end_headers()
            response = BytesIO()
            response.write(b'This is a POST request')
            response.write(b' - Received:')
            response.write(body)
            self.wfile.write(response.getvalue())
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
        return

httpd = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()