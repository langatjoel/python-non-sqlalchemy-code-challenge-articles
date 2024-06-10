class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        if not isinstance(category, str):
            raise TypeError("Category must be of type str")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._name = name
        self._category = category
        self._articles = []
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be of type str")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be of type str")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        authors = [article.author for article in self._articles]
        return [author for author in set(authors) if authors.count(author) > 2] if self._articles else None

    @classmethod
    def top_publisher(cls):
        return max(cls.all_magazines, key=lambda magazine: len(magazine._articles), default=None)
