import db

db.init_db()

# Criar
task_id = db.create_task("Comprar pão", "Pão francês na padaria")
print("Tarefa criada com ID:", task_id)

# Listar
print("Todas as tarefas:", db.list_tasks())

# Buscar por ID
print("Tarefa única:", db.get_task(task_id))

# Atualizar
db.update_task(task_id, "completo")
print("Tarefa atualizada:", db.get_task(task_id))

# Deletar
db.delete_task(task_id)
print("Após deletar:", db.list_tasks())
