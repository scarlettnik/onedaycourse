a = [[int(x) for x in input().split()] for _ in range(int(input()))]
a.sort(key = lambda a: a[1])
d=[a[0][1]]
for i in range(1, len(a)):
    if a[i][0]>d[-1]:
        d.append(a[i][1]) 
print(len(d))    
print(*d)