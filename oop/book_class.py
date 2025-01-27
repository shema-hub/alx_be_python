class Book:
    """
    A class to model a book with attributes for title, author, and publication year.
    Includes magic methods for enhanced functionality.
    """

    def __init__(self, title, author, year):
        """
        Initializes a Book instance.
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor method, prints a message when the object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation of the book.
        Returns:
            str: A string in the format "(title) by (author), published in (year)".
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation of the book.
        Returns:
            str: A string that recreates the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"


def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book


if __name__ == "__main__":
    main()
