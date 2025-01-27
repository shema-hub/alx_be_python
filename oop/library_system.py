import math

class Book:
    """
    Base class representing a book.
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Derived class representing an electronic book.
    Inherits from Book.
    Attributes:
        file_size (int): The size of the eBook file in kilobytes.
    """
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived class representing a printed book.
    Inherits from Book.
    Attributes:
        page_count (int): The number of pages in the printed book.
    """
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Class representing a library, demonstrating composition by managing a collection of books.
    Attributes:
        books (list): A list to store instances of Book, EBook, and PrintBook.
    """
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """
        Adds a Book, EBook, or PrintBook instance to the library.
        Args:
            book (Book): An instance of Book or its subclasses.
        """
        self.books.append(book)

    def list_books(self):
        """
        Prints details of each book in the library.
        """
        for book in self.books:
            print(book)


def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()


if __name__ == "__main__":
    main()
