from http.server import BaseHTTPRequestHandler
from src.config import INDEX_PATH


class MyServer(BaseHTTPRequestHandler):

    @staticmethod
    def __get_index():
        with open(INDEX_PATH, 'r') as file:
            return file.read()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(self.__get_index(), "utf-8"))
