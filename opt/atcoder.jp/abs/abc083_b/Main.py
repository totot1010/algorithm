n,a, b = map(int, input().split())

score = 0
for num in range(n+1):
    sum = 0
    for x in list(map(int, str(num))):
        sum += x

    if sum >= a and sum <= b:
        score += num
print(score)
