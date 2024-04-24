import liwc

def liwc_analyze(text):
  parse, _ = liwc.load_token_parser("../liwc/LIWC2007_Portugues_win.dic")
  return list(parse(text))