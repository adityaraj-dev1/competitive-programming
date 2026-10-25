def sumk(arr,k):
    i = 0
    j = 0
    curr_sum = 0
    maximum = 0
    while j < len(arr):
        curr_sum += arr[j]
        j+=1
        while curr_sum > k:
            curr_sum -= arr[i]
            i+= 1
        if curr_sum == k:  
          maximum = max(maximum,j-i)

    return maximum
arr = [1,2,1,1,1,3]
k = 3
print(sumk(arr,k))          

# time complexity = O(n)
# space complexity = O(1)