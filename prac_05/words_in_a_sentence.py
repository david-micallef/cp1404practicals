word_dict = {}

entered_sentence = str(input("Enter a sentence to count the number of times the words occur: "))

words = entered_sentence.split()

for i in range(len(words)):
    number_of_words = word_dict.get(words[i],0)
    if number_of_words is None:
        word_dict[words[i]] = 1
    else:
        word_dict[words[i]] = number_of_words + 1

ordered_words = list(word_dict.keys())
ordered_words.sort()

character_length = max(len(ordered_words[i]) for i in range(len(ordered_words)))

for i in range(len(ordered_words)):
    print("{:{}} : {}".format(ordered_words[i], character_length, word_dict[ordered_words[i]]))

