from implements.poo.model.SpecialTokenManipulator import SpecialTokenManipulator
from implements.poo.model.StringReader import StringReader
from implements.poo.model.TokenManipulator import TokenManipulator
# Programação Funcional (1.5pt):
# ● Você NÃO pode permitir efeitos colaterais dentro de funções.
# ● Use funções anônimas a vontade

# ● Você NÃO pode alterar o estado de forma nenhuma ( i.e., tudo é const)
# ● Não use loops. Se quiser repetição faça com funções ou com recursão.
# ● Use funções map,filter,reduce a vontade (pelo menos uma única vez)
# ● Você pode adaptar funções/métodos anteriores, desde-que aderentes ao funcional

texto = """
Felicidade é viver na sua companhia 
Felicidade é estar contigo todo dia
Felicidade é sentir o cheiro dessa flor
Felicidade é saber que eu tenho seu amor
- Seu jorge
"""

# Primeiro recebe o texto e limpo ele com o StringReader
tokenizer = StringReader(texto)
tokens = tokenizer.get_cleaned_token()
print(f"Text tokens: {tokens}")

# Depois manipulo ela com o SpecialTokenManipulator para limpar os caracteres especiais
manipulator = SpecialTokenManipulator(tokens)
tokens = manipulator.get_analyzed_tokens()
print(f"Analyzed Tokens: {tokens}")
manipulator.set_tokens(tokens)

# Filtro pelas categorias que eu desejo
swearCount = manipulator.get_category_counter("swear")
anxCount = manipulator.get_category_counter("anx")
posemoPerc = manipulator.get_category_percentage("posemo")
negemoPerc = manipulator.get_category_percentage("negemo")

print(f"Saida : {len(tokens)} palavras, {swearCount} palavras ofensivas , {anxCount} palavras de ansiedade, tom geral positivo: {posemoPerc}%, tom geral negativo: {negemoPerc:.2f}%")