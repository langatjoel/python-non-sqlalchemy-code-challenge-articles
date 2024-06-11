# test_article.py
import pytest
from lib.testing.author_test import Author
from lib.testing.magazine_test import Magazine
from lib.testing.article_test import Article

# Test Author class
def test_author_initialization():
    author = Author("John Doe")
    assert author.name == "John Doe"

def test_author_name_type():
    with pytest.raises(TypeError):
        Author(123)

def test_author_name_length():
    with pytest.raises(ValueError):
        Author("")

# Test Magazine class
def test_magazine_initialization():
    magazine = Magazine("Tech Today", "Technology")
    assert magazine.name == "Tech Today"
    assert magazine.category == "Technology"

def test_magazine_name_type():
    with pytest.raises(TypeError):
        Magazine(123, "Technology")

def test_magazine_name_length():
    with pytest.raises(ValueError):
        Magazine("", "Technology")

def test_magazine_category_type():
    with pytest.raises(TypeError):
        Magazine("Tech Today", 123)

def test_magazine_category_length():
    with pytest.raises(ValueError):
        Magazine("Tech Today", "")

# Test Article class
def test_article_initialization():
    author = Author("John Doe")
    magazine = Magazine("Tech Today", "Technology")
    article = Article(author, magazine, "The Future of AI")
    assert article.author == author
    assert article.magazine == magazine
    assert article.title == "The Future of AI"

def test_article_title_type():
    author = Author("John Doe")
    magazine = Magazine("Tech Today", "Technology")
    with pytest.raises(TypeError):
        Article(author, magazine, 123)

def test_article_title_length():
    author = Author("John Doe")
    magazine = Magazine("Tech Today", "Technology")
    with pytest.raises(ValueError):
        Article(author, magazine, "")

# Test Author methods
def test_author_articles():
    author = Author("John Doe")
    magazine = Magazine("Tech Today", "Technology")
    article = Article(author, magazine, "The Future of AI")
    assert article in author.articles()

def test_author_magazines():
    author = Author("John Doe")
    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Science Weekly", "Science")
    article1 = Article(author, magazine1, "The Future of AI")
    article2 = Article(author, magazine2, "Advancements in Science")
    assert magazine1 in author.magazines()
    assert magazine2 in author.magazines()

# Test Magazine methods
def test_magazine_articles():
    author = Author("John Doe")
    magazine = Magazine("Tech Today", "Technology")
    article = Article(author, magazine, "The Future of AI")
    assert article in magazine.articles()

def test_magazine_contributors():
    author1 = Author("John Doe")
    author2 = Author("Jane Doe")
    magazine = Magazine("Tech Today", "Technology")
    article1 = Article(author1, magazine, "The Future of AI")
    article2 = Article(author2, magazine, "Advancements in Science")
    assert author1 in magazine.contributors()
    assert author2 in magazine.contributors()

# Add more tests to achieve a total of 30 or more
def test_article_author_change():
    author1 = Author("John Doe")
    author2 = Author("Jane Doe")
    magazine = Magazine("Tech Today", "Technology")
    article = Article(author1, magazine, "The Future of AI")
    article.author = author2
    assert article.author == author2
    assert article in author2.articles()

def test_magazine_category_change():
    magazine = Magazine("Tech Today", "Technology")
    magazine.category = "Science"
    assert magazine.category == "Science"

def test_article_invalid_author():
    magazine = Magazine("Tech Today", "Technology")
    with pytest.raises(TypeError):
        Article("John Doe", magazine, "The Future of AI")

def test_article_invalid_magazine():
    author = Author("John Doe")
    with pytest.raises(TypeError):
        Article(author, "Tech Today", "The Future of AI")

