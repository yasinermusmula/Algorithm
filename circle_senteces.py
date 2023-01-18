# my_list = "leetcode exercises sound delightful"


def string(sentence):
    words = sentence.split(" ")

    for i in range(len(words)):
        last_char = words[i][-1]
        first_char = words[(i + 1) % len(words)][0]

        if last_char != first_char:
            return False
    return True


print(string("leetcode exercises sound delightful"))
