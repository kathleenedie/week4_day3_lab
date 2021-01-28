from flask import Flask, render_template, request, redirect, Blueprint
from models.book import Book
from models.author import Author

from repositories import book_repository
from repositories import author_repository

books_blueprint = Blueprint('books', __name__)

@books_blueprint.route('/books')
def get_books():
    books = book_repository.select_all()
    return render_template('books/index.html', books = books)

@books_blueprint.route('/books/<id>')
def one_book(id):
    book = book_repository.select(id)
    return render_template('books/show.html', book = book)


@books_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete(id):
    book_repository.delete(id)
    return redirect('/books')

@books_blueprint.route("/books/new", methods=['GET'])
def new_book():
    author= author_repository.select_all()
    return render_template("books/new.html", authors = author)


@books_blueprint.route('/books', methods=['POST'])
def create_book():
    first_name = request.form['author_namef']
    last_name = request.form['author_namel']
    author_new = Author(first_name, last_name)
    author = author_repository.save(author_new)
    title = request.form['title']
    genre = request.form['genre']
    publisher = request.form['publisher']
    book = Book(title, genre, publisher, author, id)
    book_repository.save(book)
    return redirect('/books')

@books_blueprint.route("/books/<id>/edit", methods=["GET"])
def edit_book(id):
    book = book_repository.select(id)
    author = author_repository.select_all()
    return render_template('books/edit.html', book = book, author = author)

@books_blueprint.route("/books/<id>", methods=["POST"])
def update_book(id):    
    title = request.form['title']
    author_id = request.form['author_id']
    genre = request.form['genre']
    publisher = request.form['publisher']
    author = author_repository.select(author_id)
    book = Book(title, publisher, genre, author, id)
    return redirect('/books')