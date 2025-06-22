
class Book:
    #"Base class for all books.
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    #Derived class representing an electronic book.
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        return f"EBook: {super().__str__()}, File Size: {self.file_size}KB"


class PrintBook(Book):
    #Derived class representing a printed book.
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook:  {super().__str__()}, Page Count: {self.page_count}"


class Library:
    #Class that manages a collection of books (composition).
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only instances of Book or its subclasses can be added.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)
