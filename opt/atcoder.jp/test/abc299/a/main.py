n = int(input())
s = input()

index_group = []
index_asterisk = None
for i in range(n):
    if s[i] == "*":
        index_asterisk = i
    if s[i] == "|":
        index_group.append(i)
    
if index_asterisk> index_group[0] and index_asterisk < index_group[1]:
    print("in")
else:
    print("out")