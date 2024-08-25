from abc import ABC, abstractmethod
from app.models import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: Book):
        pass


class ConsoleDisplay(Display):
    def __init__(self, display_type):
        self.display_type = display_type

    def display(self, book: Book):
        if self.display_type == "console":
            print(book.content)
        else:
            raise ValueError(f"Unknown display type: {self.display_type}")


class ReverseDisplay(Display):
    def __init__(self, display_type):
        self.display_type = display_type

    def display(self, book: Book):
        if self.display_type == "reverse":
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {self.display_type}")


class Print(ABC):
    @abstractmethod
    def print_book(self, book: Book):
        pass


class ConsolePrint(Print):
    def __init__(self, print_type):
        self.print_type = print_type

    def print_book(self, book: Book):
        if self.print_type == "console":
            print(f"Printing the book: {book.title}...")
            print(book.content)
        else:
            raise ValueError(f"Unknown print type: {self.print_type}")


class ReversePrint(Print):
    def __init__(self, print_type):
        self.print_type = print_type

    def print_book(self, book: Book):
        if self.print_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {self.print_type}")
