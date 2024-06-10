from testing.author import Author
from testing.magazine import Magazine
from testing.article import Article

import ipdb; ipdb.set_trace()

# Create some sample data to test
author = Author("John Doe")
magazine = Magazine("Tech Today", "Technology")
article = Article(author, magazine, "The Future of AI")
