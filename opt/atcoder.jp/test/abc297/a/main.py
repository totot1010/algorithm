
n, d = list(map(int, input().split()))
t = list(map(int, input().split()))


for i, num in enumerate(range(n)):
    if i + 1 >= n:
        print(-1)
        break
    if t[i +1] - t[i] <= d:
        print(t[i+1])
        break