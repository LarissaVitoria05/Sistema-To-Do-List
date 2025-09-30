import json
from Service import task_service

def CreateTask(path, body):
    if path.strip() == "/create":
        dados = json.loads(body)
        titulo = dados.get("titulo")
        descricao = dados.get("descricao")
        return task_service.CreateService(titulo, descricao)
    else:
        return {"codigo": 404, "mensagem": "Rota não encontrada"}
    
def ListTask(path):
    if path.strip() == "/list":
        tarefas = task_service.ListTask()  # provavelmente retorna uma lista
        return {"codigo": 200, "tarefas": tarefas}
        
    else:
        return {"codigo": 404, "mensagem": "Rota não encontrada"}

def GetTaskById(path):
 
    if path.startswith("/list-by-id"):
        try:           
            task_id = int(path.split("/")[-1])
            tarefa = task_service.GetById(task_id)
            if tarefa:
                return {"codigo": 200, "tarefa": tarefa}
            else:
                return {"codigo": 404, "mensagem": "Tarefa não encontrada"}
        except ValueError:
            return {"codigo": 400, "mensagem": "ID inválido"}
    else:
        return {"codigo": 404, "mensagem": "Rota não encontrada"}