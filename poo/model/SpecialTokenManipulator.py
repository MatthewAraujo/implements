from implements.poo.model.TokenManipulator import TokenManipulator
from implements.poo.resource.Utils import liwc_analyze
import re


class SpecialTokenManipulator(TokenManipulator):

    def __init__(self, tokens):
        super().__init__(tokens)

    def get_tokens_count(self):
        return len(self.tokens)

    def get_analyzed_tokens(self):
        cleaned_analyzed_tokens = [liwc_analyze(token) for token in self.tokens]
        return cleaned_analyzed_tokens
