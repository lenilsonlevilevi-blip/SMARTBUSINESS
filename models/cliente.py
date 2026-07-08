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