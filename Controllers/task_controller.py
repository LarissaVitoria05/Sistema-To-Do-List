import json
from Service import task_service

def CreateTask(path, body):
    if path.strip() == "/tasks":
        dados = json.loads(body)
        titulo = dados.get("titulo")
        descricao = dados.get("descricao")
        task_service.CreateService(titulo, descricao)
        res = task_service.ListTask()
        return  res
    else:
        return {"codigo": 404, "mensagem": "Rota não encontrada"}
    
def ListTask(path):
    if path.strip() == "/tasks":
        tarefas = task_service.ListTask() 
        return {"codigo": 200, "tarefas": tarefas}      
    else:
        return {"codigo": 404, "mensagem": "Rota não encontrada"}

def GetTaskById(path):
 
    if path.startswith("/tasks"):
                
            task_id = int(path.split("/")[-1])
            res = task_service.GetById(task_id)
            return res         
    else:
        return {"codigo": 404, "mensagem": "Rota não encontrada"}
    
def UpdateTask(path):
 
    if path.startswith("/tasks/"):             
            task_id = int(path.split("/")[-1])
            task_service.UpdateTask(task_id)
            res  = task_service.GetById(task_id)
            return  res
    else:
            return {"codigo": 404, "mensagem": "Rota não encontrada"}
       
def DeleteTask(path):
 
    if path.startswith("/tasks/"):             
            task_id = int(path.split("/")[-1])
            task_service.DeleteTask(task_id)
            res  = task_service.ListTask()
            return  res
    else:
            return {"codigo": 404, "mensagem": "Rota não encontrada"}
       
   