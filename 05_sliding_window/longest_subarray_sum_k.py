def longestsubaray(arr,k):
    i = 0
    j = 0
    curr_sum = 0
    maxi = 0
    while j <len(arr):
        curr_sum += arr[j]
        if j-i+1 < k:
            j+=1
        elif j-i+1 == k:
            maxi = max(maxi,curr_sum)
            curr_sum -= arr[i]
            i+=1
            j+=1
    return maxi
arr = [1, 2, 3, 1, 2, 4]
k = 3
print(longestsubaray(arr,k))        

# time complexity = O(n)
# space complexity = O(1)