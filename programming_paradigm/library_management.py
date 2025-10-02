class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def return_book(self):
        return f"{self.title}"
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def list_available_books(self):
        for book in self._books:
             print(f"{book.title} by {book.author}")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                print(f"You returned '{book.title}'.")
                return
        print(f"'{title}' was not checked out.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = True
                return f"You checked out '{book.title}'.")
                
        print(f"'{title}' is not available")

    