#OPP LIBRARY MANAGEMENT SYSTЕМ
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Patron Name: {self.name}")
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print("-", book.title)
        else:
            print("No books borrowed.")


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []


    def add_book(self):
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        new_book = Book(title, author)
        self.books.append(new_book)
        print("Book added successfully!\n")

    def show_books(self):
        if not self.books:
            print("No books available.\n")
            return

        print("\n------ Library Books ------")
        for i, book in enumerate(self.books, start=1):
            print(f"\nBook {i}")
            book.display()
        print()


    def register_patron(self):
        name = input("Enter Patron Name: ")
        new_patron = Patron(name)
        self.patrons.append(new_patron)
        print("Patron registered successfully!\n")

    def show_patrons(self):
        if not self.patrons:
            print("No patrons registered.\n")
            return

        print("\n------ Patron List ------")
        for i, patron in enumerate(self.patrons, start=1):
            print(f"\nPatron {i}")
            patron.display()
        print()


    def borrow_book(self):
        patron_name = input("Enter Patron Name: ")
        book_title = input("Enter Book Title: ")

        patron = None
        for p in self.patrons:
            if p.name.lower() == patron_name.lower():
                patron = p
                break

        if patron is None:
            print("Patron not found.\n")
            return

        for book in self.books:
            if book.title.lower() == book_title.lower():
                if book.available:
                    book.available = False
                    patron.borrowed_books.append(book)
                    print("Book issued successfully!\n")
                else:
                    print("Book is already issued.\n")
                return

        print("Book not found.\n")


    def return_book(self):
        patron_name = input("Enter Patron Name: ")
        book_title = input("Enter Book Title: ")

        for patron in self.patrons:
            if patron.name.lower() == patron_name.lower():
                for book in patron.borrowed_books:
                    if book.title.lower() == book_title.lower():
                        book.available = True
                        patron.borrowed_books.remove(book)
                        print("Book returned successfully!\n")
                        return

                print("This patron has not borrowed that book.\n")
                return

        print("Patron not found.\n")


library = Library()

while True:
    print("\n========== Library Management System ==========")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Show Books")
    print("6. Show Patrons")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.register_patron()

    elif choice == "3":
        library.borrow_book()

    elif choice == "4":
        library.return_book()

    elif choice == "5":
        library.show_books()

    elif choice == "6":
        library.show_patrons()

    elif choice == "7":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice! Please try again.")