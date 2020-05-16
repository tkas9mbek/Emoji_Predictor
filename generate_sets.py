import random

with open('us_trial.text', 'r') as data_file:
  text_data = data_file.read()
  text_list = list( text_data.split("\n") ) 

with open('us_trial.labels', 'r') as data_file:
  labels_data = data_file.read()
  label_list = list( labels_data.split("\n") ) 

sample_size = len(text_list)



def shuffle(rate = 50000):
  for i in range(0, rate):
    a = random.randint(0, sample_size - 1)
    b = random.randint(0, sample_size - 1)
    text_list[b], text_list[a] = text_list[a], text_list[b]
    label_list[b], label_list[a] = label_list[a], label_list[b]

def split( train_ratio = 0.9 ):
  train_text = text_list[0: int(sample_size * train_ratio)]
  train_label = label_list[0: int(sample_size * train_ratio)]
  test_text = text_list[int(sample_size * train_ratio) :]
  test_label = label_list[int(sample_size * train_ratio) :]
  return train_text, train_label, test_text, test_label
