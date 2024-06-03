# author_test.py

import pytest
from many_to_many import Author, Article, Magazine

class TestAuthor:
    def test_has_name(self):
        """Author is initialized with a name"""
        author = Author("John Doe")
        assert author.name == "John Doe"

    def test_name_is_immutable_string(self):
        """author name is of type str and cannot change"""
        author = Author("John Doe")
        with pytest.raises(AttributeError):
            author.name = "Jane Doe"

    def test_name_len(self):
        """author name is longer than 0 characters"""
        with pytest.raises(ValueError):
            Author("")

    # Other test methods for Author class...

if __name__ == "__main__":
    pytest.main()
