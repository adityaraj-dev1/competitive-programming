import sys
def main():
    data = sys.stdin.read().split()
    n = data[0]
    count = 0
    max_count = 0
    for i in range(1,len(n)):
        if n[i-1] == n[i]:
            count +=1
        else:
            count = 0
        max_count = max(count,max_count)      
    if max_count >= 6:
        print("Yes")
    else:
        print("No")                
main()

