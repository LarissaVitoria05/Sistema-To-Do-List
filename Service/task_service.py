from Repository  import task_repository


def CreateService(titulo, descricao): 
    res = task_repository.CreateRepository(titulo, descricao)
    return res