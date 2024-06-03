# many_to_many.py

class Author:
    def __init__(self, name):
        self.name = name
        self.articles = []
        self.magazines = []

    def add_article(self, title, content):
        article = Article(title, content)
        self.articles.append(article)
        return article

    def get_topic_areas(self):
        topic_areas = set()
        for article in self.articles:
            topic_areas.update(article.topic_areas)
        return list(topic_areas)

class Article:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.author = None
        self.magazines = []
        self.topic_areas = set()

    def set_author(self, author):
        self.author = author

    def set_magazine(self, magazine):
        self.magazines.append(magazine)

    def add_topic_area(self, topic):
        self.topic_areas.add(topic)

class Magazine:
    def __init__(self, name):
        self.name = name
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)
        article.set_magazine(self)

    def get_articles(self):
        return self.articles
