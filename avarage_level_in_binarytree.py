
# Find Missing Element
def findMissing(arr, N):

    # create a list of zeroes
    temp = [0] * (N+1)

    for i in range(0, N):
        temp[arr[i] - 1] = 1

    for i in range(0, N+1):
        if(temp[i] == 0):
            ans = i + 1

    print(ans)

# Driver code
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 8]
    N = len(arr)

    # Function call
    findMissing(arr, N)

    # This code is contributed by nikhilm2302