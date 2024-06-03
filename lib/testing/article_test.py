# article_test.py

import pytest
from many_to_many import Author, Article, Magazine

class TestArticle:
    def test_has_title(self):
        """Article is initialized with a title"""
        article = Article("Title", "Content")
        assert article.title == "Title"

    def test_title_is_immutable_str(self):
        """title is an immutable string"""
        article = Article("Title", "Content")
        with pytest.raises(AttributeError):
            article.title = "New Title"

    def test_title_is_valid(self):
        """title is between 5 and 50 characters inclusive"""
        with pytest.raises(ValueError):
            Article("A", "Content")
        with pytest.raises(ValueError):
            Article("A" * 51, "Content")

    # Other test methods for Article class...

if __name__ == "__main__":
    pytest.main()
