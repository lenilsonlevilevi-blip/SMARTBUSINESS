from flask import Blueprint, render_template

financeiro = Blueprint("financeiro", __name__)


@financeiro.route("/financeiro")
def index():
    return render_template("financeiro.html")