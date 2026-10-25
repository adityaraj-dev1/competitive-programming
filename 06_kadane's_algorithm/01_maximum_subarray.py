def max_subarray(arr):
    i = 0
    best_ending= arr[0]
    ans = arr[0]
    for i in range(1,len(arr)):
        v1 = arr[i]
        v2 = best_ending + arr[i]
        best_ending = max(v1,v2)
        ans = max(ans,best_ending)
    return ans
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(arr))    

# time complexity = O(n)
# space complexity = O(1)