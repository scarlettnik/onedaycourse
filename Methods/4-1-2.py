n, w = list(map(int, input().split()))
items = [list(map(int, input().split())) for i in range(n)]
items = sorted(items, key=lambda i: i[0]/i[1], reverse=True)
c = 0
while w and items:
    item = items.pop(0)
    packed = min(item[1], w)
    c += packed*item[0]/item[1]
    w -= packed
print(c)