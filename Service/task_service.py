from Repository  import task_repository


def CreateService(titulo, descricao): 
    
    if not titulo or not descricao:
        return {"codigo": 400, "mensagem": "Título e descrição são obrigatórios"}   
    
    res = task_repository.CreateRepository(titulo, descricao)
    if not res:
            return {"codigo":404, "mensagem": "Tarefa não foi criada"}
    return res

def ListTask():
    res = task_repository.ListTask()
    if not res:
        return {"codigo": 404, "mensagem": "Nenhuma tarefa encontrada"}
    return  res

def GetById(id):
    if not id:
        return {"codigo": 404, "mensagem": "Id necessario"}
    res = task_repository.GetByID(id)
    if not res:
        return {"codigo": 404, "mensagem": "Nenhuma tarefa encontrada"}
    return   res
         