from collections.abc import Generator
from typing import Annotated

from classes_and_object.utils.logger import *
from classes_and_object.shames.book_shame import BookShame

__all__ = ['logger']


class Library:
    """
    Класс для добавления, удаления и вывода всех книг
    """
    def __init__(self) -> None:
        self._books: Annotated[list[BookShame], "Список с книгами"] = []

    # Метод для добавления книги
    def add_book(self, book: BookShame) -> None:
        self._books.append(book)
        logger.debug("Добавлена книга по ID: {}, с названием: {}", book.book_id, book.name)

    def print_all_books(self) -> None:
        """
        Проверяем не пустой ли список с книгами
        если он пуст то, выбрасывает исключение
        """
        if not self._books:
            logger.error("List with books is empty")
            raise

        # Выводим все книги
        logger.info('----------- All books -----------')
        for book in self._books:
            logger.info(f"ID: {book.book_id}: {book.name}")
        logger.info('---------------------------------')

    def delete_book(self, book_id: int) -> None:
        for book in self._books:
            if book.book_id == book_id:
                remove_book = self._books.pop(book_id)
                logger.debug('Book with ID: {} is delete', book_id)
                logger.debug('Delete a book: {}', remove_book)
                return

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

