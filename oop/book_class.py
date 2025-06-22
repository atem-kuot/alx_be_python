class Book:
    def __init__(self, title, author, year):
        """Initialize the Book with title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints a message when the Book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation of the Book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Unambiguous string representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
class Book:
    def __init__(self, title, author, year):
        """Initialize the Book with title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints a message when the Book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation of the Book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Unambiguous string representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
