# library_system.py
# Kevin Pavione
# January 20, 2026
# Assignment 2: Library Management System
"""
A library management system demonstrating OOP principles:
inheritance, polymorphism, and encapsulation.
"""

class LibraryItem:
    """Base class for all library items."""

    def __init__(self, title, item_id):
        """Initialize a library item."""
        self._title = title
        self._item_id = item_id
        self._is_checked_out = False
        self._checked_out_by = None

    def get_title(self):
        """Return the title of the item."""
        return self._title

    def get_item_id(self):
        """Return the unique item ID."""
        return self._item_id

    def is_available(self):
        """Return True if the item is available for checkout."""
        return not self._is_checked_out

    def check_out(self, patron_name):
        """
        Check out the item to a patron.
        Returns True if successful, False if already checked out.
        """
        if self.is_available():
            self._is_checked_out = True
            self._checked_out_by = patron_name
            return True
        return False

    def return_item(self):
        """
        Return the item to the library.
        Returns True if successful, False if not checked out.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            self._checked_out_by = None
            return True
        return False

    def get_details(self):
        """Return basic item details (to be overridden)."""
        status = "Available" if self.is_available() else f"Checked out to {self._checked_out_by}"
        return (f"Title: {self._title}\n"
                f"ID: {self._item_id}\n"
                f"Status: {status}")


class Book(LibraryItem):
    """A book in the library collection."""

    def __init__(self, title, item_id, author, isbn, pages):
        """Initialize a book with book-specific attributes."""
        super().__init__(title, item_id)
        self.author = author
        self.isbn = isbn
        self.pages = pages

    def get_details(self):
        """Return detailed information about the book."""
        status = "Available" if self.is_available() else f"Checked out to {self._checked_out_by}"
        return (f"Title: {self._title}\n"
                f"ID: {self._item_id}\n"
                f"Type: Book\n"
                f"Author: {self.author}\n"
                f"ISBN: {self.isbn}\n"
                f"Pages: {self.pages}\n"
                f"Status: {status}\n")


class DVD(LibraryItem):
    """A DVD in the library collection."""

    def __init__(self, title, item_id, director, runtime, rating):
        """Initialize a DVD with DVD-specific attributes."""
        super().__init__(title, item_id)
        self.director = director
        self.runtime = runtime
        self.rating = rating

    def get_details(self):
        """Return detailed information about the DVD."""
        status = "Available" if self.is_available() else f"Checked out to {self._checked_out_by}"
        return (f"Title: {self._title}\n"
                f"ID: {self._item_id}\n"
                f"Type: DVD\n"
                f"Director: {self.director}\n"
                f"Runtime: {self.runtime} minutes\n"
                f"Rating: {self.rating}\n"
                f"Status: {status}\n")


class Magazine(LibraryItem):
    """A magazine in the library collection."""

    def __init__(self, title, item_id, issue_number, publication_date):
        """Initialize a magazine with magazine-specific attributes."""
        super().__init__(title, item_id)
        self.issue_number = issue_number
        self.publication_date = publication_date

    def get_details(self):
        """Return detailed information about the magazine."""
        status = "Available" if self.is_available() else f"Checked out to {self._checked_out_by}"
        return (f"Title: {self._title}\n"
                f"ID: {self._item_id}\n"
                f"Type: Magazine\n"
                f"Issue: #{self.issue_number}\n"
                f"Publication Date: {self.publication_date}\n"
                f"Status: {status}\n")


class Library:
    """Manages a collection of library items."""

    def __init__(self, name):
        """Initialize a library with a name and empty item list."""
        self.name = name
        self.items = []

    def add_item(self, item):
        """Add a library item to the collection."""
        self.items.append(item)

    def find_item(self, item_id):
        """Find and return item by ID, or None if not found."""
        for item in self.items:
            if item.get_item_id() == item_id:
                return item
        return None

    def check_out_item(self, item_id, patron_name):
        """Check out an item by ID to a patron."""
        item = self.find_item(item_id)
        if item is None:
            print(f"Item not found: {item_id}")
            return False
        if item.check_out(patron_name):
            print(f"Successfully checked out: {item.get_title()} to {patron_name}")
            return True
        else:
            print(f"Item not available: {item.get_title()}")
            return False

    def return_item(self, item_id):
        """Return an item by ID."""
        item = self.find_item(item_id)
        if item is None:
            print(f"Item not found: {item_id}")
            return False
        if item.return_item():
            print(f"Successfully returned: {item.get_title()}")
            return True
        else:
            print(f"Item was not checked out: {item.get_title()}")
            return False

    def list_available_items(self):
        """Return list of titles of available items."""
        return [item.get_title() for item in self.items if item.is_available()]

    def list_checked_out_items(self):
        """Return list of titles + patron of checked out items."""
        return [f"{item.get_title()} (by {item._checked_out_by})"
                for item in self.items if not item.is_available()]

    def display_catalog(self):
        """Print detailed catalog of all items."""
        for item in self.items:
            print(item.get_details())
            print()  # blank line between items


def main():
    """Demonstrate the library management system."""
    print("===================================")
    print("LIBRARY MANAGEMENT SYSTEM")
    print("===================================\n")

    # Create library
    library = Library("Oakland City University Library")
    print(f"Library Name: {library.name}\n")

    print("--- Adding Items to Catalog ---")

    # Books
    book1 = Book("1984", "BOOK001", "George Orwell",
                 "978-0451524935", 328)
    book2 = Book("To Kill a Mockingbird", "BOOK002", "Harper Lee",
                 "978-0060935467", 336)

    # DVDs
    dvd1 = DVD("The Matrix", "DVD001", "The Wachowskis", 136, "R")
    dvd2 = DVD("Inception", "DVD002", "Christopher Nolan", 148, "PG-13")

    # Magazines
    mag1 = Magazine("National Geographic", "MAG001", 245, "January 2026")
    mag2 = Magazine("Time Magazine", "MAG002", 12, "December 2025")

    items_to_add = [book1, book2, dvd1, dvd2, mag1, mag2]

    for item in items_to_add:
        library.add_item(item)
        print(f"Added: {item.get_title()} ({item.get_item_id()})")

    print("\n--- Checking Out Items ---")
    library.check_out_item("BOOK001", "Alice Smith")
    library.check_out_item("DVD001", "Bob Johnson")
    library.check_out_item("MAG001", "Alice Smith")
    library.check_out_item("BOOK001", "Charlie Brown")  # already checked out

    print("\n--- Returning Items ---")
    library.return_item("BOOK001")
    library.return_item("BOOK002")  # wasn't checked out

    print("\n--- Complete Catalog ---")
    library.display_catalog()

    print("--- Available Items ({}) ---".format(len(library.list_available_items())))
    available = library.list_available_items()
    for i, title in enumerate(available, 1):
        print(f"  {i}. {title}")

    print("\n--- Checked Out Items ({}) ---".format(len(library.list_checked_out_items())))
    checked_out = library.list_checked_out_items()
    for i, info in enumerate(checked_out, 1):
        print(f"  {i}. {info}")

    print("\n===================================")
    print("END OF REPORT")
    print("===================================")


if __name__ == "__main__":
    main()
