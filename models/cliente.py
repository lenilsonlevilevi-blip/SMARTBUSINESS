from database.database import conectar


def criar_tabela_clientes():

    banco = conectar()

    banco.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT,
            email TEXT,
            cidade TEXT
        )
    """)

    banco.commit()
    banco.close()

def buscar_clientes():

    banco = conectar()

    clientes = banco.execute("""
        SELECT * FROM clientes
    """).fetchall()

    banco.close()

    return clientes

def adicionar_cliente(nome, telefone, email, cidade):

    banco = conectar()

    banco.execute("""
        INSERT INTO clientes (nome, telefone, email, cidade) VALUES (?, ?, ?, ?)
    """, (nome, telefone, email, cidade))

    banco.commit()
    banco.close()