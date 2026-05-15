
from src.features.pages.bookstore import BookStore
from src.features.pages.favorite_books import FavoriteBooks


def test_add_book_to_favorites():

    store = BookStore()

    favorites = FavoriteBooks()

    book = store.addBook("Kent Beck", "TDD")

    favorites.add(book)

    assert len(favorites.books) == 1


def test_remove_book_from_favorites():

    store = BookStore()

    favorites = FavoriteBooks()

    book = store.addBook("Kent Beck", "TDD")

    favorites.add(book)

    favorites.remove(book)

    assert len(favorites.books) == 0

