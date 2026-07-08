from flask import Blueprint, render_template, request, redirect
from models.cliente import buscar_clientes, adicionar_cliente


clientes = Blueprint("clientes", __name__)


@clientes.route("/clientes")
def index():

    lista_clientes = buscar_clientes()

    return render_template(
        "clientes.html",
        clientes=lista_clientes
    )


@clientes.route("/clientes/novo", methods=["GET", "POST"])
def novo():

    if request.method == "POST":

        nome = request.form["nome"]
        telefone = request.form["telefone"]
        email = request.form["email"]
        cidade = request.form["cidade"]

        adicionar_cliente(
            nome,
            telefone,
            email,
            cidade
        )

        return redirect("/clientes")

    return render_template("novo_cliente.html")