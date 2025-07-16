#DUNDER METHODS
import datetime
today = datetime.datetime.now()
today
datetime.datetime(2023, 10, 1, 12, 0, 0)
print(today)  # Output: 2023
str(today)  # Output: '2023-10-01 12:00:00'

# book.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

odyssey = Book("The Odyssey", "Homer")

print(odyssey)
# book.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

odyssey = Book("The Odyssey", "Homer")

print(repr(odyssey))
print(str(odyssey))
# book.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(title={self.title!r}, author={self.author!r})"

odyssey = Book("The Odyssey", "Homer")

print(repr(odyssey))
print(str(odyssey))
# book.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(title={self.title!r}, author={self.author!r})"

    def __str__(self):
        return f'"{self.title}" by {self.author}'

odyssey = Book("The Odyssey", "Homer")

print(repr(odyssey))
print(str(odyssey))

