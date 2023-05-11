W, H, x, y, r = map(int, input().split())

a, b, c, d, e = [5, 4, 2, 2, 1]

if x >= r and x <= W-r and y >= r and y <= H-r:
    print('Yes')
else:
    print('No')