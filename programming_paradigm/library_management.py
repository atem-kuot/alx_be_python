class Book:
    def __init__(self, title, author, _is_checked_out ):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out
    

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title} by {book.author}.")

    def return_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print(f"Returned book: {book.title} by {book.author}.")
        else:
            print("Book already exists in the library.")

    def check_out_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Removed book: {book.title} by {book.author}.")
        else:
            print("Book not found in the library.")

    def list_available_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            for book in self.books:
                status = "Checked out" if book._is_checked_out else "Available"
                print(f"{book.title} by {book.author} - {status}")
