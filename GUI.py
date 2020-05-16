from tkinter import *
import model
import generate_sets
import create_bag_of_words


with open('us_mapping.txt', 'r') as data_file:
  emoji_data = data_file.read()
  emoji_list = list( emoji_data.split("\n") ) 

  for i in range(len(emoji_list)):
    emoji_list[i] = emoji_list[i][2:].replace("\t", " ")

print(emoji_list)

generate_sets.shuffle()

train_text, train_label, test_text, test_label = generate_sets.split(1)

word_list, word_list_indices = create_bag_of_words.generate(train_text)

train_size = len(train_text)
test_size = len(test_text)
feature_size = len(word_list)

probs_label, probs_label_feature = model.train_model(feature_size, train_label, train_text, word_list_indices)

window = Tk()
window.title("Emoji Predictor")
window.geometry('720x480')

lbl = Label(window, text="Enter Text", font=("Monospace", 18))
lbl.grid(column=4, row=2)

txt = Entry(window, width=30, font=("Monospace", 18))
txt.grid(column=4, row=3)

emoji1 = Label(window, text="#1 ", fg="red", font=("Monospace", 20))
emoji1.grid(column=4, row=6)

emoji2 = Label(window, text="#2 ", fg="red", font=("Monospace", 20))
emoji2.grid(column=4, row=7)

emoji3 = Label(window, text="#3 ", fg="red", font=("Monospace", 20))
emoji3.grid(column=4, row=8)

def clicked():
  predicted = model.predict_one(txt.get(), word_list_indices, probs_label, feature_size, probs_label_feature)
  
  emoji1.configure(text = u"#1 " + emoji_list[ predicted [0]],  font=("Monospace", 20))
  emoji2.configure(text = u"#2 " + emoji_list[ predicted [1]],  font=("Monospace", 20))
  emoji3.configure(text = u"#3 " + emoji_list[ predicted [2]],  font=("Monospace", 20))

btn = Button(window, text = "Get emoji", command = clicked, font=("Monospace", 20))
btn.grid(column=4, row=4)

window.mainloop()