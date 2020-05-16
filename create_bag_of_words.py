import word_trimmer
import re

def isOK(insput_str):
  if( len(insput_str) < 4 or len(insput_str) > 12 ):
    return False
  if insput_str.isalpha():
    return True
  return False

def is_ascii(insput_str):
    return all(ord(c) < 128 for c in insput_str)

def add_word(w, bag_of_words):
  w = word_trimmer.trim(w)
  if w not in word_trimmer.stop_words and isOK(w) and is_ascii(w):
    bag_of_words.add(w.lower()) 

def generate(train_text):
  bag_of_words = set()

  for text in train_text:
    for w in word_trimmer.word_tokenize(text): 
      if '#' in w:
        if( len(w) < 8):
          add_word(w, bag_of_words)
        else:
          words = re.findall('[A-Z][^A-Z]*', w)
          for hashw in words:
            add_word(hashw, bag_of_words)
      else:
        add_word(w, bag_of_words) 

  word_list = list(bag_of_words)
  word_list_indices = {}
  feature_size = len(word_list)

  for i in range(0, feature_size):
    word_list_indices[ word_list[i] ] = i

  with open('bag_of_words.txt', 'w') as outfile:
    outfile.write(repr(bag_of_words))
    outfile.close()

  return word_list, word_list_indices