a = int(input())
b = list(map(int, input().split()))

count = 0

def devideNumber(b, count, a):
    list = []
    for num in b:
        if num % 2 == 0:
            new_num = num / 2
            list.append(new_num)
        else:
            print(count)
            return

    if len(list) == a:
        count +=1
        devideNumber(list, count, a)



devideNumber(b, count, a)