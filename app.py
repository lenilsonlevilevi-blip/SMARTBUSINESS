from flask import Flask
from models.cliente import criar_tabela_clientes
from routes.dashboard import dashboard
from routes.clientes import clientes
from routes.produtos import produtos
from routes.financeiro import financeiro

app = Flask(__name__)

app.register_blueprint(dashboard)
app.register_blueprint(clientes)
app.register_blueprint(produtos)
app.register_blueprint(financeiro)

criar_tabela_clientes()

if __name__ == "__main__":
    app.run(debug=True)