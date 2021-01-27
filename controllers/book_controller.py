from flask import Flask, render_template, request, redirect, Blueprint
from models.book import Book
from models.author import Author

from repositories import book_repository

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


