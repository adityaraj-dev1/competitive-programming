def maxproduct(arr):
    i = 0
    min_ending = arr[0]
    max_ending = arr[0]
    ans = arr[0]
    for i in range(1,len(arr)):
        v1 = arr[i]
        v2 = min_ending*arr[i]
        v3 = max_ending*arr[i]
        min_ending = min(v1,v2,v3)
        max_ending = max(v1,v2,v3)
        ans = max(ans,max(min_ending,max_ending))
    return ans
arr = [2,3,-2,4]
print(maxproduct(arr))    

# time complexity = O(n)
# space complexity = O(1)