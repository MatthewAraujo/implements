import os
from utils import liwc_analyze

# Programação Estruturada (1.5pt):
# ● Os únicos métodos de manipulação de strings que você pode usar são: split,
# append, join e length. Todo o resto (modificações, remoções) deve ser feito com
# loops.
# ● Organize suas funções como quiser.
# ● Organize seus dados como quiser.jc


def stringCleaner(text):
  special_words = [33, 34, 35, 36, 37, 38, 42, 43, 45, 47, 58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 125, 126, 199]
  cleaned_text = ""
  for char in text:
    if ord(char) == 199:
      cleaned_text += "C"
    if ord(char) not in special_words:
      cleaned_text += char
  return cleaned_text


def stringLower(text):
  upper_case_ascii = [chr(i) for i in range(65, 91)]
  lower_string = ""
  for word in text:
    if word in upper_case_ascii:
      lower_string += chr(ord(word) + 32)
    else:
      lower_string += word
  return lower_string

def stringReader(text): 
  return text.split()

def tokenManipulator(tokens):
  return [liwc_analyze(token) for token in tokens]
  
def liwcCounter(tokens):
  categories = {}
  for token in tokens:
    for category in token:
      if category in categories:
        categories[category] += 1
      else:
        categories[category] = 1
  return categories

def category_counter(tokens, category):
  count = 0
  for token in tokens:
    if category in token:
      count += 1
  return count

def openFile(path_file):
  return open(path_file, "r", encoding="utf8")


def main(path_file):
  text = openFile(path_file)
  cleaned_text = stringCleaner(text.read())
  lower_text = stringLower(cleaned_text)
  tokens = stringReader(lower_text)
  tokens = tokenManipulator(tokens)
  posemoCount = (category_counter(tokens, "posemo") / len(tokens) ) * 100
  negemoCount = (category_counter(tokens, "negemo") / len(tokens) ) * 100 
  swearCount = category_counter(tokens, "swear")
  anxCount = category_counter(tokens, "anx")
  print(f"Saida : {len(tokens)} palavras,{swearCount} palavras ofensivas ,{anxCount} palavras de ansiedade, tom geral positivo: {posemoCount:.2f}%, tom geral negativo: {negemoCount:.2f}%")


if __name__ == "__main__":
  main("./fe/texto")

  
