def sum_of_diognal_array(array):
    sum_left = 0
    sum_right = 0
    j = len(array) - 1
    for i in range(len(array)):
        sum_left += array[i][i]
        sum_right += array[i][j]
        j -= 1

    return sum_left, sum_right


print(sum_of_diognal_array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]]))
