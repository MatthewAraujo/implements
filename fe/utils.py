import liwc

def liwc_analyze(text):
  parse, category_names = liwc.load_token_parser("./liwc/LIWC2007_Portugues_win.dic")
  return list(parse(text))