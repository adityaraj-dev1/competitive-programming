def maxaverage(arr,k):
    i = 0
    j = 0
    summ = 0
    max_average = float('-inf')
    while j < len(arr):
        summ += arr[j]
        if j-i+1 < k:
           j+=1
        elif j-i+1 == k:
           average = summ/k
           max_average = max(average,max_average)
           summ -= arr[i]
           i+=1
           j+=1
    return max_average
arr = [1,12,-5,-6,50,3]
k = 4
print(maxaverage(arr,k))       

# time complexity = O(n)
# space complexity = O(1)