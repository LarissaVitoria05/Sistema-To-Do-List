from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from Controllers import task_controller

class SimpleServer(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        resultado = task_controller.CreateTask(self.path, body)
        self._send_response(resultado)

    def do_PATCH(self):
            resultado = task_controller.UpdateTask(self.path)
            self._send_response(resultado)
            
    def do_DELETE(self):
            resultado = task_controller.DeleteTask(self.path)
            self._send_response(resultado)

    def do_GET(self):
        if self.path.strip() == "/list":
            resultado = task_controller.ListTask(self.path)
            self._send_response(resultado)
        elif self.path.startswith("/list-by-id/"):
            resultado = task_controller.GetTaskById(self.path)
            self._send_response(resultado)
        else:
            resultado = {"codigo": 404, "mensagem": "Rota não encontrada"}
            self._send_response(resultado)
    def do_GET_by_id(self):
        resultado = task_controller.GetTaskById(self.path)
        self._send_response(resultado)

    def _send_response(self, resultado):
        
        self.send_response(resultado.get("codigo", 500))
        
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
