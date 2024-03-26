from utils import liwc_analyze

# Programação Estruturada (1.5pt):
# ● Os únicos métodos de manipulação de strings que você pode usar são: split,
# append, join e length. Todo o resto (modificações, remoções) deve ser feito com
# loops.
# ● Organize suas funções como quiser.
# ● Organize seus dados como quiser.

def stringReader(text): 
  return text.split()

def tokenManipulator(tokens):
  return [liwc_analyze(token) for token in tokens]

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


text = """
Felicidade é viver na sua companhia
Felicidade é estar contigo todo dia
Felicidade é sentir o cheiro dessa flor
Felicidade é saber que eu tenho seu amor
"""

tokens = stringReader(text)
tokens = tokenManipulator(tokens)
categories = liwcCounter(tokens)
swearCount = categories.get("swear", 0)
anxCount = categories.get("anx", 0)

print(f"Saida : {len(tokens)} palavras,{swearCount} palavras ofensivas ,{anxCount} palavras de ansiedade,")

