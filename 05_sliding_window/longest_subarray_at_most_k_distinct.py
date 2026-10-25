def longest_subarray_k(arr,k):
    i = 0
    j = 0
    maximum = 0
    freq = {}
    while j < len(arr):
        freq[arr[j]] = freq.get(arr[j],0)+1
        j+=1
        while len(freq) > k:
            freq[arr[i]] -= 1
            if freq[arr[i]] == 0:
                del freq[arr[i]]
            i+=1        
        maximum = max(maximum,j-i)   
    return maximum
arr = [1, 2, 1, 2, 3]
k = 2
print(longest_subarray_k(arr,k))             

# time complexity = O(n)
# space complexity = O(k)




        

        
