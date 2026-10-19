import sys
def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    for i in range(1,n+1):
        word = data[i]
        if len(word) <= 10:
            print(word)
        else:
            first = word[0]
            last = word[-1]
            middle = str(len(word) - 2)
            print(first+middle+last)
main()


