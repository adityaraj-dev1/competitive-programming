def flipping_zeroes(arr):
    i = 0
    j = 0
    zeros = 0
    maximum = 0

    while j < len(arr):

        if arr[j] == 0:
            zeros += 1

        j += 1

        while zeros > 1:
            if arr[i] == 0:
                zeros -= 1
            i += 1

        maximum = max(maximum, j - i)

    return maximum

# time complexity = O(n)
# space complexity = O(1)

