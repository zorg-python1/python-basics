# Define a custom exception class
class BookAlreadyBorrowedException(Exception):
    def __init__(self, book_title):
        super().__init__(f"The book '{book_title}' is already borrowed.")

# Function to borrow a book
def borrow_book(book_title, borrowed_books):
    if book_title in borrowed_books:
        raise BookAlreadyBorrowedException(book_title)
    else:
        borrowed_books.append(book_title)
        print(f"The book '{book_title}' has been successfully borrowed.")

# Test the function
borrowed_books = ["Python Programming", "Data Science Essentials"]
try:
    borrow_book("Python Programming", borrowed_books)
except BookAlreadyBorrowedException as e:
    print(e)
