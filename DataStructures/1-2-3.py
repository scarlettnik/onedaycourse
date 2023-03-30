import bisect
size, n = map(int, input().split())
e = []
for i in range(n):
    arrival, duration = map(int, input().split())
    del e[0:bisect.bisect(e, arrival)] 
    if len(e) < size:
        begin = max(e[-1], arrival) if e else arrival
        print(begin)
        e.append(begin + duration)
    else:
        print(-1)