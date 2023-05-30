n = int(input())
w = list(input().split())

judge = None
for str in w:
    if "and" == str or "not"  == str or "that" == str or "the" == str or "you" == str:
        judge = "Yes"
        print(judge)
        break

if judge is None:
    print("No")

