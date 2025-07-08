from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://uwpbrzasi4dzqlld8ekl:B7ADHjpsKnVUWKu71i9aBDA7oOlyEY@bbqhgph7wb0iza3ajqzn-postgresql.services.clever-cloud.com:50013/bbqhgph7wb0iza3ajqzn'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

from models.author import Author
from models.genre import Genre
from models.book import Book

@app.route('/authors')
def authors():
    authors = Author.query.all()
    authors_dict = []
    for author in authors:
        authors_dict.append(author.dict())
    return jsonify(authors_dict)

@app.route('/authors/<int:id>')
def author(id):
    author = Author.query.get(id)
    return jsonify(author.dict())

@app.route('/authors-by-name/<name>')
def author_by_name(name):
    authori = Author.query.filter_by(name=name)
    authors_dict = []
    for author in authori:
        authors_dict.append(author.dict())
    return jsonify(authors_dict)

@app.route('/authors', methods=['POST'])
def add_author():
    data = request.json
    author = Author()
    author.name = data['name']
    author.bio = data['bio']
    db.session.add(author)
    db.session.commit()
    return jsonify(author.dict())

@app.route('/books')
def books():
    books = Book.query.all()
    return "test"

if __name__ == '__main__':
    app.run(debug=True)
