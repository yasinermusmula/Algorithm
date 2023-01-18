
array = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]

for i in range(2):
    first_best_score = 0
    for num in array:
        if num > first_best_score:
            first_best_score = num
    array.remove(first_best_score)
    print(first_best_score)

