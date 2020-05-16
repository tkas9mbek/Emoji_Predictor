import model
import generate_sets
import create_bag_of_words

model

# Main

generate_sets.shuffle()

train_text, train_label, test_text, test_label = generate_sets.split(0.90)

word_list, word_list_indices = create_bag_of_words.generate(train_text)

train_size = len(train_text)
test_size = len(test_text)
feature_size = len(word_list)


print(feature_size)

probs_label, probs_label_feature = model.train_model(feature_size, train_label, train_text, word_list_indices)

# Test model
predicted_labels = model.predict(test_text, probs_label, probs_label_feature, test_label, word_list_indices, feature_size)

accuracy = model.test(predicted_labels, test_label)

print("accuracy:", accuracy)