def max_vowels(s,k):
    vowels = ["a","e","i","o","u"]
    max_count = 0
    count = 0
    i = 0
    for j in range(len(s)):
        if s[j] in vowels:
            count +=1
        if j-i+1 == k:
           max_count = max(count,max_count)
           if s[i] in vowels:
              count -= 1
           i+=1
    return max_count
s = "abciiidef" 
k = 3          
print(max_vowels(s,k))      

# time complexity = O(n)
# space complexity = O(1)