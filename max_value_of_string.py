"""Input: strs = ["alic3","bob","3","4","00000"]
Output: 5
Explanation:
- "alic3" consists of both letters and digits, so its value is its length, i.e. 5.
- "bob" consists only of letters, so its value is also its length, i.e. 3.
- "3" consists only of digits, so its value is its numeric equivalent, i.e. 3.
- "4" also consists only of digits, so its value is 4.
- "000001" consists only of digits, so its value is 0.
Hence, the maximum value is 5, of "alic3"."""


def max_value_of_string(array):
    max_value = len(array[0])

    for element in array:
        if not element.isdigit():
            value = len(element)
        else:
            value = int(element)

        if max_value < value:
            max_value = value

    return max_value


print(max_value_of_string(["alic3", "bob678", "35", "4", "00000"]))
