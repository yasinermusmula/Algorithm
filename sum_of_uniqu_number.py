def sum_of_unique_number(nums):
    result = 0
    for i in nums:
        if nums.count(i) == 1:
            result += i
    return result


print(sum_of_unique_number([5, 2, 3, 2]))
