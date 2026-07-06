from flask import Blueprint, render_template

produtos = Blueprint("produtos", __name__)


@produtos.route("/produtos")
def index():
    return render_template("produtos.html")