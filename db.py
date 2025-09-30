import sqlite3

DB_NAME = "tarefas.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT,
                status TEXT DEFAULT 'pendente',
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

def create_task(titulo, descricao, status="pendente"):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tarefas (titulo, descricao, status) VALUES (?, ?, ?)",
                    (titulo, descricao, status))
        conn.commit()
        return cur.lastrowid

def list_tasks():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM tarefas")
        return cur.fetchall()

def get_task(task_id):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM tarefas WHERE id = ?", (task_id,))
        return cur.fetchone()

def update_task(task_id, status):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("UPDATE tarefas SET status = ? WHERE id = ?", (status, task_id))
        conn.commit()
        return cur.rowcount

def delete_task(task_id):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM tarefas WHERE id = ?", (task_id,))
        conn.commit()
        return cur.rowcount
