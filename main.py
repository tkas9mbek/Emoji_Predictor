import json

exclude_set = {
  "A woman is a female human",
  "Female adult human",
  "An animal of the sex that produces eggs",
  "An adult human member of the sex that produces ova and bears young",
  "An adult female human",
  "An adult female person (as opposed to a man)",
  "Adult female human being",
  "Sexual maturity is the age or stage when an organism can reproduce",
  "The age or stage when an organism can reproduce",
  "An adult male human",
  "A man is a male human",
  "An adult male human",
  "An adult human member of the sex that begets young by fertilizing ova",
  "A human member of the masculine sex or gender",
  "An adult person who is male (as opposed to a woman)"
}

def filter_values(word_type):
  for senses in element['senses'][word_type]:
    for sense in senses[list(senses.keys())[0] ]:
      sense = sense.replace(".", "")
      if sense not in exclude_set:
        write_data[emoji_code].append(sense)

write_data = {}

with open('emojis.json', 'r') as data_file:
  json_data = data_file.read()

data = json.loads(json_data)
 
for element in data:
  try:
    emoji_code = element['unicode'][:element['unicode'].index(" ")]
  except ValueError:
    emoji_code = element['unicode']
  
  write_data[emoji_code] = []

  filter_values("adjectives")
  filter_values("verbs")
  filter_values("nouns")

with open('training_set.json', 'w') as outfile:
    json.dump(write_data, outfile)