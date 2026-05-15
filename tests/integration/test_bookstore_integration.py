
from src.features.pages.bookstore import BookStore


def test_add_book_and_toggle_favorite_flow():

    store = BookStore()

    # Add book
    book = store.addBook("John Grisham", "The Pelican Brief")

    # Toggle favorite
    store.toggleFavorite(book["id"])

    # Verify
    assert book["favorite"] is True

