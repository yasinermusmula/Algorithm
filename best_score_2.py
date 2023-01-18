def first_second_score(array):
    best_score = 0
    second_score = 0
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            if array[i] > best_score:
                second_score = best_score
                best_score = array[i]
            if array[i + 1] > second_score:
                second_score = array[i + 1]
        else:
            if array[i + 1] > best_score:
                second_score = best_score
                best_score = array[i + 1]
            if array[i] > second_score:
                second_score = array[i]
    return best_score, second_score


my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second_score(my_list))