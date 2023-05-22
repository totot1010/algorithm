N = int(input())
S = input()
T = S.count("T")
A = S.count("A")

if T > A:
    print("T")
elif T == A:
    if S[-1] == "T":
        print("A")
    else:
        print("T")
else:
    print("A")