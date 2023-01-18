def matrix_diagonal_sum(array):
    array_first_sum = 0
    array_second_sum = 0
    var_j = len(array) - 1

    for i in range(len(array)):
        array_first_sum += array[i][i]
        array_second_sum += array[i][var_j]
        var_j -= 1
    return array_first_sum,array_second_sum


print(matrix_diagonal_sum([[3, 2, 3],
                           [4, 3, 6],
                           [7, 8, 8]]))
