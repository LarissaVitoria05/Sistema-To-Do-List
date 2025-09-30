
import db

db.init_db()

def CreateRepository(titulo, descricao):
    res = db.create_task(titulo, descricao)
    return res


def ListTask():
    res = db.list_tasks()
    return res

def GetByID(task_id):
    res = db.get_task(task_id)
    return res