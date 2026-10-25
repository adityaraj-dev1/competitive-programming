def minsize(arr,target):
    min_size = float('inf')
    summ = 0
    i = 0
    for j in range(len(arr)):
        summ += arr[j]
        while summ >= target:
            min_size = min(min_size,j-i+1)
            summ -= arr[i]
            i+=1    
    return 0 if min_size == float('inf') else min_size
arr = [2,3,1,2,4,3]
target = 7
print(minsize(arr,target))            

# time complexity = O(n)
# space complexity = O(1)