import string

alphabet = list(string.ascii_lowercase)
values = [i for i in range(len(alphabet))] # list compheration
myDict = {k: v for (k, v) in zip(alphabet, values)} # Dict compheration


def odd_string_difference(words):
    length_of_word = len(words[0])
    global_difference = []
    answer = 0
    for i in range(len(words)):
        local_difference = []
        for j in range(length_of_word - 1):
            difference = myDict[words[i][j + 1]] - myDict[words[i][j]]
            local_difference.append(difference)
        if local_difference not in global_difference and len(global_difference) > 0:
            answer = words[i]
            global_difference.append(local_difference)
        else:
            global_difference.append(local_difference)
    return answer



print(odd_string_difference(["adc","wzy","abc"]))