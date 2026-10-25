def check(s1,s2):
    if len(s1) > len(s2):
        return False
    need = {}
    for ch in s1:
        need[ch] = need.get(ch,0)+1
    i = 0
    freq = {}
    for j in range(len(s2)):
        freq[s2[j]] = freq.get(s2[j],0)+1
        while j-i+1 > len(s1):
            freq[s2[i]] -= 1
            if freq[s2[i]] == 0:
                del freq[s2[i]]
            i+=1
        if j-i+1 == len(s1):
            if need == freq:
                return True
    return False                   

s1 = "ab"
s2 = "eidbaooo"
print(check(s1,s2))

# let N = len(s1) and M = len(s2)
# time complexity = O(N*M)
# space complexity = O(M)