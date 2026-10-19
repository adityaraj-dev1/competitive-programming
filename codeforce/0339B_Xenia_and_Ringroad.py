import sys
def main():
    data = sys.stdin.read().split()
    n,m = int(data[0]), int(data[1])
    works = list(map(int,data[2:2+m]))

    current = 1
    total = 0
    for work in works:
        target = work
        if current > target:
            time = n - current+target
        else:
            time = target - current
        total += time
        current = target
    print(total)        

main()            