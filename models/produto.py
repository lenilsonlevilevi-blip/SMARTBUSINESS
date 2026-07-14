from database.database import conectar


def criar_tabela_produtos():
    banco = conectar()

    banco.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            codigo TEXT,
            categoria TEXT,
            preco_compra REAL,
            preco_venda REAL,
            estoque INTEGER,
            estoque_minimo INTEGER
        )
    """)

    banco.commit()
    banco.close()


def buscar_produtos():
    banco = conectar()

    produtos = banco.execute("""
        SELECT * FROM produtos
        ORDER BY nome
    """).fetchall()

    banco.close()

    return produtos

def adicionar_produto(
    nome,
    codigo,
    categoria,
    preco_compra,
    preco_venda,
    estoque,
    estoque_minimo
):
    banco = conectar()

    banco.execute("""
        INSERT INTO produtos (
            nome,
            codigo,
            categoria,
            preco_compra,
            preco_venda,
            estoque,
            estoque_minimo
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        nome,
        codigo,
        categoria,
        preco_compra,
        preco_venda,
        estoque,
        estoque_minimo
    ))

    banco.commit()
    banco.close()