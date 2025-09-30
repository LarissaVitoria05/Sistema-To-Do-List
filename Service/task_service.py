from Repository  import task_repository


def CreateService(titulo, descricao): 
    
    if not titulo or not descricao:
        return {"codigo": 400, "mensagem": "Título e descrição são obrigatórios"}   
 
    res = task_repository.CreateRepository(titulo, descricao)
    
    return {"codigo": 201, "mensagem": "Tarefa criada com sucesso", "resultado": res}
