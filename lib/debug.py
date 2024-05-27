#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article, Author, Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Create sample instances for testing
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")

    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")

    article1 = Article(author1, magazine1, "The Future of AI")
    article2 = Article(author1, magazine2, "Healthy Living Tips")
    article3 = Article(author2, magazine1, "The Rise of Quantum Computing")
    article4 = Article(author2, magazine1, "Cybersecurity in 2024")
    article5 = Article(author1, magazine1, "AI and Healthcare")

    # Test methods
    print(author1.name)
    print(magazine1.name)
    print(article1.title)

    print(author1.articles())  # Should list all articles by John Doe
    print(author1.magazines())  # Should list all magazines John Doe has written for

    print(magazine1.articles())  # Should list all articles in Tech Today
    print(magazine1.contributors())  # Should list all contributors to Tech Today

    print(magazine1.article_titles())  # Should list titles of all articles in Tech Today
    print(magazine1.contributing_authors())  # Should list authors with more than 2 articles in Tech Today

    print(author1.topic_areas())  # Should return a unique list of categories

    # Add a new article via author
    new_article = author1.add_article(magazine2, "Mental Health Matters")
    print(new_article.title)  # Should print "Mental Health Matters"

    # Don't remove this line, it's for debugging!
    ipdb.set_trace()
