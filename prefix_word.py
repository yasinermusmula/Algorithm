def prefix_word(sentence, search_word):
    sentence = sentence.split(" ")
    word_len = len(search_word)
    for i in range(len(sentence)):
        word = sentence[i]
        if len(word) >= word_len and search_word == word[:word_len]:
            return i + 1
    return -1


print(prefix_word("I like eat burger", "bur"))
