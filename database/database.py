import sqlite3
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(BASE_DIR, "smartbusiness.db")


def conectar():
    banco = sqlite3.connect(CAMINHO_BANCO)
    banco.row_factory = sqlite3.Row
    return banco