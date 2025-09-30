
import db

db.init_db()

def CreateTask(titulo, descricao):
    res = db.create_task(titulo, descricao)
    return res


def ListTask():
    res = db.list_tasks()
    return res

def GetByIDTask(task_id):
    res = db.get_task(task_id)
    return res

def  UpdateTask(id):
    res = db.update_task(id, "completo")
    return res