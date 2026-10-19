import sys
def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1]
    count = 0
    for i in range(1,len(s)):
        if s[i-1] == s[i]:
            count +=1
    print(count)
main()
