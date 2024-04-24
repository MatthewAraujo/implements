# ● Consumir textos de APIs de redes sociais (twitter,facebook,etc..).
import praw
from functools import reduce
from utils import liwc_analyze

def stringCleaner(text):
  special_words = set([33, 34, 35, 36, 37, 38, 42, 43, 45, 47, 58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 125, 126, 199])
  print("ola stringcleaner")
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

def get_reddit_posts(subreddit_name, limit):
    # Autenticação no Reddit
    reddit = praw.Reddit(client_id='seu_id',
                         client_secret='seu_secret',
                         user_agent='MeuBot')

    # Fórum escolhido
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    # Tratando as postagens
    for submission in subreddit.hot(limit=limit):
        text = submission.selftext

        cleaned_text = stringCleaner(text)
        lower_text = stringLower(cleaned_text)
        text_tokens = transformStringToToken(lower_text)

        posts.append(text_tokens)

    return posts

def main(subreddit_name, limit):
    print("obtendo postagens...")
    posts = get_reddit_posts(subreddit_name, limit)

    if not posts:
        print("Postagens não encontradas no subreddit!")
        return

    print("analisando postagens...")
    total_words = 0
    total_swear = 0
    total_anx = 0
    total_posemo = 0
    total_negemo = 0

    for i, (text_tokens) in enumerate(posts, start=1):
        total_words += len(text_tokens)
        total_swear += category_counter(text_tokens, "swear")
        total_anx += category_counter(text_tokens, "anx")
        total_posemo += category_counter(text_tokens, "posemo")
        total_negemo += category_counter(text_tokens, "negemo")


    total_posts = len(posts)
    total_posemo_percentage = (total_posemo / total_words) * 100
    total_negemo_percentage = (total_negemo / total_words) * 100

    print(f"Subreddit: /r/{subreddit_name}")
    print(f"Total de posts: {total_posts:.2f}")
    print(f"Total de palavras: {total_words:.2f}")
    print(f"Total de palavras ofensivas: {total_swear:.2f}")
    print(f"Total de palavras de ansiedade: {total_anx:.2f}")
    print(f"Tom geral positivo: {total_posemo_percentage:.2f}%")
    print(f"Tom geral negativo: {total_negemo_percentage:.2f}%")

if __name__ == "__main__":
    main("python", 1)
