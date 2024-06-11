class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def topic_areas(self):
        topic_areas = list(set(article.magazine.category for article in self.articles()))
        return topic_areas if topic_areas else None

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not isinstance(category, str):
            raise TypeError("Name and category must be strings")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        if len(category) == 0:
            raise ValueError("Category must have length greater than 0")
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        if len(value) == 0:
            raise ValueError("Category must have length greater than 0")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles() if article.title]
        return titles if titles else None

    def contributing_authors(self):
        authors = [author for author in self.contributors() if len(author.articles()) > 2]
        return authors if authors else []
