from django.urls import path
from .views import list_books, LibraryDetailView
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Role-based views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    # Required literal URL substrings
    path('books/add_book/', add_book, name='add_book'),         # <-- changed
    path('books/edit_book/<int:book_id>/', edit_book, name='edit_book'),  # <-- changed
    path('books/delete_book/<int:book_id>/', delete_book, name='delete_book'),
]
