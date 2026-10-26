def maxsum(arr):
    i = 0
    nodeletion = arr[0]
    onedeletion = float('-inf')
    ans = arr[0]
    for i in range(1,len(arr)):
        prevnodeletion = nodeletion
        nodeletion = max(arr[i],nodeletion+arr[i])
        onedeletion = max(prevnodeletion, onedeletion+arr[i])
        ans = max(ans,nodeletion,onedeletion)
    return ans    
arr = [1,-2,0,3]
print(maxsum(arr))    

# time complexity = O(n)
# space complexity = O(1)