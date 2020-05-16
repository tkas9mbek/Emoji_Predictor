import word_trimmer
import math 
import numpy

n_classes = 20

def find_prob_label(train_label):
  train_size = len(train_label)
  probs_label = numpy.zeros(n_classes)
  for element in train_label:
    probs_label[int(element)] += 1

  for i in range(0, n_classes):
    probs_label[i] /= train_size

  return probs_label

def find_probs_label_feature(feature_size, train_label, train_text, word_list_indices):
  
  train_size = len(train_text)
  probs_label_feature = numpy.zeros(n_classes * feature_size).reshape((n_classes, feature_size))
  label_count = [0] * n_classes

  for element in train_label:
    label_count[int(element)] += 1

  for i in range(0, train_size):
    text = train_text[i]
    label = int(train_label[i])

    for word in word_trimmer.word_tokenize(text): 
      word = word_trimmer.trim(word)
      if word.lower() in word_list_indices:
        word_index = word_list_indices[word.lower()]
        probs_label_feature[label][word_index] += 1
  
  for i in range(0, n_classes):
    for j in range(0, feature_size):
        probs_label_feature[i][j] /= label_count[i]

  return probs_label_feature
  
def take_log(x):
  if x <= 0:
    return -999
  else:
    return math.log2(x)

def predict_one(text, word_list_indices, probs_label, feature_size, probs_label_feature):
  found_words = set()
  label_probailitis = [None] * n_classes

  for word in word_trimmer.word_tokenize(text): 
    word = word_trimmer.trim(word)
    if word.lower() in word_list_indices:
      word_index = int(word_list_indices[word.lower()])
      found_words.add(word_index)

  for label in range(0, n_classes):
    prob = probs_label[label]
    for feature_index in range(0, feature_size):
      if feature_index in found_words:
        prob += take_log(probs_label_feature[label][feature_index])
      else:
        prob += take_log(1 - probs_label_feature[label][feature_index])
    label_probailitis[label] = prob

  return numpy.argpartition(label_probailitis, -3)[-3:]

def train_model(feature_size, train_label, train_text, word_list_indices):
  probs_label_feature = find_probs_label_feature(feature_size, train_label, train_text, word_list_indices)
  probs_label = find_prob_label(train_label)

  return probs_label, probs_label_feature

def predict(test_text, probs_label, probs_label_feature, test_label, word_list_indices, feature_size):
  test_size = len(test_text)
  predicted_labels = [None] * test_size

  for i in range(0, test_size):
    text = test_text[i]
    found_words = set()
    label_probailitis = [None] * n_classes

    for word in word_trimmer.word_tokenize(text): 
      word = word_trimmer.trim(word)
      if word.lower() in word_list_indices:
        word_index = int(word_list_indices[word.lower()])
        found_words.add(word_index)
    
    for label in range(0, n_classes):
      prob = probs_label[label]
      for feature_index in range(0, feature_size):
        if feature_index in found_words:
          prob += take_log(probs_label_feature[label][feature_index])
        else:
          prob += take_log(1 - probs_label_feature[label][feature_index])
      label_probailitis[label] = prob

    predicted_labels[i] = numpy.argpartition(label_probailitis, -3)[-3:]

    # print(text)
    # print("Predicted:", predicted_labels[i], "Actual:", test_label[i])
    # print(label_probailitis)
    
  return predicted_labels


def test(predicted_labels, actual_labels):
  test_size = len(actual_labels)
  true = 0
  false = 0

  for i in range(0, test_size):
    if actual_labels[i] == str(predicted_labels[i][0]) or actual_labels[i] == str(predicted_labels[i][1]) or actual_labels[i] == str(predicted_labels[i][2]):
      true += 1
    else:
      false += 1

  accuracy = true / (true + false)
  return accuracy



