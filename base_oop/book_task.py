from typing import Annotated


class Book:
    def __init__(
            self,
            title: Annotated[str, 'title a book'],
            author: Annotated[str, "author a book"],
            pages: Annotated[int, "number of pages"]
    ) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self) -> str:
        return f"Book: {self.title} | author: {self.author} | pages={self.pages}"
    
    # проверяем является ли книга романом
    def is_novel(self) -> bool:
        if self.pages >= 100:
            return True
        return False

    def display_info_book(self) -> dict[str, str | int]:
        return {
            "title": self.title,
            "author": self.author,
            "pages": self.pages
        }

def main() -> None:
    book1 = Book("Евгений Онегин", "А.С.П", 200)
    print(book1.is_novel())
    print(book1.display_info_book())
    print(book1)

if __name__ == "__main__":
    main()
