import yaml, os.path
from .app import db

books = yaml.safe_load(
    open(os.path.join(os.path.dirname(__file__), "data.yml")))

# Pour avoir un id
i = 0
for book in books:
    book['id'] = i
    i += 1


def get_sample():
    return books[0:20]


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    title = db.Column(db.String(100))
    url = db.Column(db.String(200))
    img = db.Column(db.String(200))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author", backref=db.backref("books", lazy="dynamic"))
