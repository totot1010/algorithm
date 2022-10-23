n = input()
a = list(map(int, input().split()))


alice = 0
bob = 0
sorted_list = sorted(a, reverse=True)

for i, num in enumerate(sorted_list):
    if i % 2 == 0:
        alice += num
    else:
        bob += num

last = alice - bob
print(last)