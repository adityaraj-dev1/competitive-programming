def char_replace(s,k):
    i = 0
    count = 0
    res = 0
    freq = {}
    for j in range(len(s)):
        freq[s[j]] = freq.get(s[j],0)+1
        count = max(count, freq[s[j]])
        while j-i+1 - count > k:
            freq[s[i]] -= 1
            i += 1
        res = max(res,j-i+1) 
    return res
s = "AABABBA"
k = 1
print(char_replace(s,k))       

# time complexity = O(n)
# space complexity = O(Σ), or O(1) for a fixed-size character set        
