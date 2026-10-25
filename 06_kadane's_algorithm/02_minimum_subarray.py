def min_subarray(arr):
    i = 0
    ending = arr[0]
    ans = arr[0]
    for i in range(1,len(arr)):
        v1 = arr[i]
        v2 = ending + arr[i]
        ending = min(v1,v2)
        ans = min(ans,ending)
    return ans
arr = [2,1,-2,-1,-3,1,-5]
print(min_subarray(arr))

# time complexity = O(n)
# space complexity = O(1)