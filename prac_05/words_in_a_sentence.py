word_dict = {}

entered_sentence = input("Text: ")

words = entered_sentence.split()

for word in words:
    number_of_words = word_dict.get(word, 0)
    word_dict[word] = number_of_words + 1

words = list(word_dict.keys())
words.sort()

character_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, character_length, word_dict[word]))
