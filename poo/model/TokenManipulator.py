from implements.poo.model.StringReader import *
from implements.poo.resource.Utils import liwc_analyze


class TokenManipulator:

    def __init__(self, tokens):
        self.tokens = tokens

    def get_tokens(self):
        return self.tokens

    def set_tokens(self, tokens):
        self.tokens = tokens

    def get_tokens_count(self):
        return len(self.tokens)

    def get_analyzed_tokens(self):
        return [liwc_analyze(token) for token in self.tokens]

    def liwc_counter(self):
        categories = {}
        for token in self.tokens:
            for category in token:
                if category in categories:
                    categories[category] += 1
                else:
                    categories[category] = 1
        return categories

    def get_category_counter(self, category):
        count = 0
        for token in self.tokens:
            if category in token:
                count += 1
        return count

    def get_category_percentage(self, category):
        total = self.get_tokens_count()
        percentage = ((self.get_category_counter(category)) / total) * 100
        return round(percentage, 2)
