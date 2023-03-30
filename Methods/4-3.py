import heapq
heap = []
for i in range(int(input())):
    s = input()
    if s[:6] == 'Insert': heapq.heappush(heap,(-1)*int(s[7:])) 
    else: print(-heapq.heappop(heap))