
from src.features.pages.bookstore import BookStore
from src.features.pages.favorite_books import FavoriteBooks


def test_add_book():

    store = BookStore()

    book = store.addBook("Martin Fowler", "Refactoring")

    assert len(store.books) == 1
    assert book["author"] == "Martin Fowler"
    assert book["title"] == "Refactoring"


def test_toggle_favorite():

    store = BookStore()

    book = store.addBook("Robert Martin", "Clean Code")

    store.toggleFavorite(book["id"])

    assert book["favorite"] is True


def test_add_to_favorites():

    favorites = FavoriteBooks()

    book = {
        "title": "Python"
    }

    favorites.add(book)

    assert len(favorites.books) == 1


def test_remove_from_favorites():

    favorites = FavoriteBooks()

    book = {
        "title": "Python"
    }

    favorites.add(book)

    favorites.remove(book)

    assert len(favorites.books) == 0

