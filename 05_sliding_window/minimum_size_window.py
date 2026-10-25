def min_size(s,t):
    need = {}
    for ch in t:
        need[ch] = need.get(ch,0)+1
    i = 0
    freq = {}
    start = 0
    res = float('inf')
    for j in range(len(s)):
        freq[s[j]] = freq.get(s[j],0)+1
        while all(freq.get(ch,0) >= need[ch] for ch in need):
            if j-i+1 < res:
              res = j-i+1
              start = i
            freq[s[i]] -= 1
            i += 1
    if res == float('inf'):
        return ""       
    return s[start:start+res]

s = "ADOBECODEBANC" 
t = "ABC"
print(min_size(s,t))   

# time complexity = O(N*M)
# space complexity = O(N+M)