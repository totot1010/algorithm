n = int(input())
a = list(map(int, input().split()))
l = []
for b in a:
    if b % 2 == 0:
        print(b)