# -*- coding: utf-8 -*-
"""LMS2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/195gsy4MoZ_dxd99DKxBdixLged1Km1jt
"""

class Student:
    def request_book(self):
        print("Enter the name of the book you want to borrow: ")
        self.book = input()
        return self.book

    def return_book(self):
        print("Enter the name of the book you want to return: ")
        self.book = input()
        return self.book

class Library:
    def __init__(self, list_of_books):
        self.available_books = list_of_books

    def display_available_books(self):
        print("Books present in this library are: ")
        for book in self.available_books:
            print(book)

    def borrow_book(self, requested_book):
        if requested_book in self.available_books:
            print(f"You have been issued '{requested_book}'")
            self.available_books.remove(requested_book)

        else:
            print("Sorry, book not available")

    def return_book(self, returned_book):
        self.available_books.append(returned_book)
        print(f"Thank you for returning '{returned_book}'")

def main():
    library = Library(["book1", "book2", "book3", "book4", "book5"])
    student = Student()
    done = False

    while not done:
        print("1. Display all books")
        print("2. Request a book")
        print("3. Return a book")
        print("4. Exit")

        try:
            user_choice = int(input("Enter your choice: "))

            if user_choice == 1:
                library.display_available_books()

            elif user_choice == 2:
                requested_book = student.request_book()
                library.borrow_book(requested_book)

            elif user_choice == 3:
                returned_book = student.return_book()
                library.return_book(returned_book)

            elif user_choice == 4:
                done = True
                print("Thank you")
            else:
                print("Invalid")

# Run the program
if __name__ == "__main__":
    main()