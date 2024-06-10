from .author import Author
from .magazine import Magazine

class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        if not isinstance(title, str):
            raise TypeError("Title must be of type str")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters, inclusive")
        
        self._author = author
        self._magazine = magazine
        self._title = title

        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @property
    def title(self):
        return self._title

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("author must be an instance of Author")
        self._author._articles.remove(self)
        self._author = value
        self._author._articles.append(self)

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        self._magazine._articles.remove(self)
        self._magazine = value
        self._magazine._articles.append(self)
