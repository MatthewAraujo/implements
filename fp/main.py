from functools import reduce
from utils import liwc_analyze

def stringCleaner(text):
  special_words = set([33, 34, 35, 36, 37, 38, 42, 43, 45, 47, 58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 125, 126, 199])
  return ''.join(filter(lambda char: ord(char) not in special_words, text))

def stringLower(text):
  upper_case_ascii = set([chr(i) for i in range(65, 91)])
  return ''.join(map(lambda word: chr(ord(word) + 32) if word in upper_case_ascii else word, text))

def stringReader(text):
  return text.split()

def tokenManipulator(tokens):
  return list(map(liwc_analyze, tokens))

def transformStringToToken(text):
  text = stringReader(text)
  return tokenManipulator(text)

def liwcCounter(tokens):
  return reduce(lambda categories, token: {category: categories.get(category, 0) + 1 for category in token}, tokens, {})

def category_counter(tokens, category):
  return reduce(lambda count, token: count + (1 if category in token else 0), tokens, 0)

def openFile(path_file):
  with open(path_file, "r", encoding="utf8") as file:
    return file.read()

def main(path_file):
  text = openFile(path_file)
  cleaned_text = stringCleaner(text)
  lower_text = stringLower(cleaned_text)
  tokens = transformStringToToken(lower_text)
  num_tokens = len(tokens)
  posemoCount = (category_counter(tokens, "posemo") / num_tokens) * 100
  negemoCount = (category_counter(tokens, "negemo") / num_tokens) * 100
  swearCount = category_counter(tokens, "swear")
  anxCount = category_counter(tokens, "anx")
  print(f"Saida : {num_tokens} palavras,{swearCount} palavras ofensivas ,{anxCount} palavras de ansiedade, tom geral positivo: {posemoCount:.2f}%, tom geral negativo: {negemoCount:.2f}%")

if __name__ == "__main__":
  main("./texto2.txt")
  main("./texto.txt")
