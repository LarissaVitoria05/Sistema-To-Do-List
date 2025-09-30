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
                
            task_id = int(path.split("/")[-1])
            res = task_service.GetById(task_id)
            return {"codigo": 200, "tarefa": res}
           
    else:
        return {"codigo": 404, "mensagem": "Rota não encontrada"}
    
def UpdateTask(path):
 
    if path.startswith("/update/"):             
            task_id = int(path.split("/")[-1])
            task_service.UpdateTask(task_id)
            tarefaUpdate  = task_service.GetById(task_id)
            return {"codigo": 200, "tarefa": tarefaUpdate}
    else:
            return {"codigo": 404, "mensagem": "Rota não encontrada"}
       
   