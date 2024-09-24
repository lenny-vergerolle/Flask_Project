from .app import app
from flask import render_template
from .models import get_sample
import yaml, os.path

data = yaml.safe_load(open(os.path.join(os.path.dirname("tuto/"), "data.yml")))

books = data[10]


def get_data():
    return books[0]


@app.route("/")
def home():
    return render_template("home.html", title="My Books !", books=get_sample())


@app.route("/livres=")
def livres():
    return render_template("livres.html", title="Livres !", livres=get_data())


#data = yaml.full_load(open("./tuto/data.yml"))


@app.route("/detail/<id>")
def detail(id):
    books = get_sample()
    book = books[int(id)]

    return render_template("detail.html", book=book)
