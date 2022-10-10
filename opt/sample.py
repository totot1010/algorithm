n = 7
a = [50, 30, 50, 100, 50, 80, 30]

list = sorted(a, reverse=True)
count = 0
before_num = 0
for i,  num in enumerate(list):
    if i == 0:
        count += 1
    if before_num > num:
        count += 1
    before_num = num


print(count)