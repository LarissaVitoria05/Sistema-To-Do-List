from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from Controllers import task_controller

class SimpleServer(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        resultado = task_controller.CreateTask(self.path, body)

        self.send_response(resultado["codigo"])
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(resultado).encode())

    def do_GET(self):
        
        resultado = task_controller.ListTask(self.path)
       

        self.send_response(resultado.get("codigo", 500))  # caso não tenha código, usa 500
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(resultado).encode())

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleServer)
    print("Servidor rodando na porta 8000")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
