# def divide_into_arr(array):
#     my_dict = {}
#
#     for i in range(len(array)):
#         if array[i] not in my_dict:
#             my_dict[array[i]] = 1
#         else:
#             my_dict[array[i]] += 1
#
#     for key, value in my_dict.items():
#         if value % 2 != 0:
#             return False
#     return True
#
#
# print(divide_into_arr([3, 2, 3, 2, 2, 2, 1]))

def fib(n):
    if n < 0:
        return -1
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    for i in range(6):
        print(fib(i), end=" ")
