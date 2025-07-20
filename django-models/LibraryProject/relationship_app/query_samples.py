# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.get(name="Chinua Achebe")
books_by_author = Book.objects.filter(author=author)
print("Books by Chinua Achebe:")
for book in books_by_author:
    print(book.title)

# 2. List all books in a library
library = Library.objects.get(name="Main City Library")
print(f"\nBooks in {library.name}:")
for book in library.books.all():
    print(book.title)

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"\nLibrarian for {library.name}: {librarian.name}")
