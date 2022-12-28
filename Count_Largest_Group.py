"""You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size."""


def slice_number(number):
    str_number = str(number)
    length_of_number = len(str_number)

    my_division = 0
    for i in range(length_of_number - 1, -1, -1):
        divide = number // (10 ** i)
        number = number % (10 ** i)
        my_division += divide
    return my_division

def count_largest_group(nums):

    group_list = []

    for num in nums:
        rakamlar_toplami = slice_number(num)

        if rakamlar_toplami

print(slice_number(13))
