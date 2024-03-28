from implements.poo.model.TokenManipulator import TokenManipulator
from implements.poo.resource.Utils import liwc_analyze
import re


class SpecialTokenManipulator(TokenManipulator):

    def __init__(self, tokens):
        super().__init__(tokens)

    def get_tokens_count(self):
        return len(self.tokens)

    def get_analyzed_tokens(self):
        cleaned_tokens = self.remove_special_tokens()
        cleaned_analyzed_tokens = [liwc_analyze(token) for token in cleaned_tokens]
        return cleaned_analyzed_tokens

    def get_special_tokens(self):
        special_words = {33, 34, 35, 36, 37, 38, 42, 43, 45, 47, 58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96,
                         123, 124, 125, 126, 199}
        special_tokens = []
        for token in self.tokens:
            for char in token:
                if ord(char) in special_words:
                    special_tokens.append(token)
                    break
        return special_tokens

    def remove_special_tokens(self):
        special_tokens = self.get_special_tokens()
        cleaned_tokens = []
        for token in self.tokens:
            if token not in special_tokens:
                cleaned_tokens.append(token)
        return cleaned_tokens