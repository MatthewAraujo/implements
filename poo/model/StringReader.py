import re


class StringReader:
    
    def __init__(self, text):
        self.text = text

    def to_lower_case(self, text):
        upper_case_ascii = [chr(i) for i in range(65, 91)]
        lower_string = ""
        for word in text:
            if word in upper_case_ascii:
                lower_string += chr(ord(word) + 32)
            else:
                lower_string += word
        return lower_string
  
    @staticmethod
    def tokenize(text): 
        return text.split()

    def get_cleaned_token(self):
        cleaned_text = self.to_lower_case(self.text)
        return self.tokenize(cleaned_text)
