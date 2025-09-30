import json
from Service import task_service

def CreateTask(path, body):
    if path.strip() == "/tarefas":
        dados = json.loads(body)
        titulo = dados.get("titulo")
        descricao = dados.get("descricao")
        return task_service.CreateService(titulo, descricao)
    else:
        return {"codigo": 404, "mensagem": "Rota não encontrada"}
