from flask import Blueprint, render_template, request, redirect

from models.produto import (
    buscar_produtos,
    adicionar_produto,
    buscar_produto_id,
    editar_produto
)

produtos = Blueprint("produtos", __name__)


@produtos.route("/produtos")
def index():

    lista_produtos = buscar_produtos()
    for produto in lista_produtos:
        print(dict(produto))

    return render_template(
        "produtos.html",
        produtos=lista_produtos
    )


@produtos.route("/produtos/novo", methods=["GET", "POST"])
def novo_produto():

    if request.method == "POST":

        adicionar_produto(
            request.form["nome"],
            request.form["codigo"],
            request.form["categoria"],
            request.form["preco_compra"],
            request.form["preco_venda"],
            request.form["estoque"],
            request.form["estoque_minimo"]
        )

        return redirect("/produtos")

    return render_template("novo_produto.html")

@produtos.route("/produtos/editar/<int:id>", methods=["GET", "POST"])
def editar_produto_route(id):
    if request.method == "POST":

        editar_produto(
            id,
            request.form["nome"],
            request.form["codigo"],
            request.form["categoria"],
            request.form["preco_compra"],
            request.form["preco_venda"],
            request.form["estoque"],
            request.form["estoque_minimo"]
        )

        return redirect("/produtos")

    produto = buscar_produto_id(id)

    return render_template(
        "editar_produto.html",
        produto=produto
    )