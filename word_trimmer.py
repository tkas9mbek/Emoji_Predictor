import nltk
nltk.download("stopwords")
nltk.download("punkt")
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

def trim(inputString):
  if inputString.endswith("-"):
    inputString = inputString[:-1]

  if inputString.endswith("s"):
    inputString = inputString[:-1]

  if len(inputString) > 2 and inputString[-2] == "'":
    inputString = inputString[:-2]

  inputString = inputString.replace("…", "").replace("...", "").replace(".", "").replace("#", "").replace("@", "").replace("\\", "").replace(".", "").replace("#", "").replace("\"", "").replace("'", "")
  
  str_len = len(inputString) - 1;

  if str_len <= 1:
    return ""
    
  new_str = ""
  for i in range(str_len):
    if inputString[i] != inputString[i + 1]:
      new_str += inputString[i]

  new_str += inputString[str_len]
  return new_str

stop_words = set(stopwords.words('english'))

punctuation = {"user"}
stop_words.update(punctuation)