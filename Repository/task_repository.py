import db

db.init_db()

def CreateRepository(titulo, descricao):
      res = db.create_task(titulo, descricao)
      return res