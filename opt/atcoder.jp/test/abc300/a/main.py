n, a, b = map(int, input().split())
l = list(map(int, input().split()))

sum_num = a + b
index = l.index(sum_num)
print(index + 1)