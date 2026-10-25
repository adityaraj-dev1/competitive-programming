def max_fruits(arr,k):
    freq = {}
    max_count = 0
    i = 0
    j = 0
    for j in range(len(arr)):
        freq[arr[j]] = freq.get(arr[j],0)+1
        while len(freq) > k:
            freq[arr[i]] -= 1
            if freq[arr[i]] == 0:
                del freq[arr[i]]
            i+=1
        max_count = max(max_count,j-i+1)
    return max_count

# time complexity -- O(n)             
# space complexity -- O(1)             