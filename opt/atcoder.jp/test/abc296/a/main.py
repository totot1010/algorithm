n = int(input())
s = input()

judge = None
for i, ss in enumerate(s):
    if i == 0:
        if n == 1:
            continue
        if s[i + 1] == ss:
            judge = "No"
    elif n == i + 1:
        if s[i - 1] == ss:
            judge = "No"
    elif s[i - 1] == ss or s[i + 1] == ss:
        judge = "No"

if judge is None:
    print("Yes")
else:
    print(judge)