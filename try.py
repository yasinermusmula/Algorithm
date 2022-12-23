def find_pivot_index(array):
    for i in range(len(array)):
        if sum(array[:i]) == sum(array[i + 1:]):
            return f"The index of pivot: {i} "
    return f"There is no index of pivot"


print(find_pivot_index([1, 7, 3, 6, 5, 6]))
