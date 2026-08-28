from collections.abc import Generator
from typing import Annotated

from pydantic import BaseModel

from base_oop.utils.logger import logger


class BookShame(BaseModel):
    book_id: int
    name: str
    description: str | None = None

class Library:
    """Класс для добавления, удаления и вывода всех книг"""
    def __init__(self) -> None:
        self._books: Annotated[list[BookShame], "Список с книгами"] = []

    # Метод для добавления книги
    def add_book(self, book: BookShame) -> None:
        self._books.append(book)
        logger.debug("Добавлена книга по ID: {}, с названием: {}", book.book_id, book.name)

    # Выводим все книги
    def print_all_books(self) -> None:
        if not self._books:
            logger.error("List with books is empty")
            raise

        logger.info('----------- All books -----------')
        for book in self._books:
            logger.info(f"ID: {book.book_id}: {book.name}")
        logger.info('---------------------------------')

    def delete_book(self, book_id: int):
        for book in self._books:
            if book.book_id == book_id:
                remove_book = self._books.pop(book_id)
                logger.debug('Book with ID: {} is delete', book_id)
                logger.debug('Delete a book: {}', remove_book)
                return
        #print("Book with ID: {book_id} not fount")

def get_valid_books() -> Generator:
    books = [
        {
            "book_id": 1,
            "name": "Преступление и наказание",
            "description": None
        },
        {
            'book_id': 2,
            'name': 'Эссенциализм',
            'description': "Жить проще но лучше"
        }
    ]
    get_books = (BookShame(**book) for book in books)
    return get_books

lib = Library()
books_valid = get_valid_books()
for book in books_valid:
    lib.add_book(book)

lib.print_all_books()

