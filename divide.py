def divide_into_arr(array):
    my_dict = {}

    for i in range(len(array)):
        if array[i] not in my_dict:
            my_dict[array[i]] = 1
        else:
            my_dict[array[i]] += 1

    for key, value in my_dict.items():
        if value % 2 != 0:
            return False
    return True


print(divide_into_arr([3, 2, 3, 2, 2, 2, 1]))
