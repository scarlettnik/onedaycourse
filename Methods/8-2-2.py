import bisect

n = int(input())
numbers = list(map(int, input().split()))
size = n * [0]
last_elem = [numbers[-1]] + [float('inf')] * (n - 1)

for i in range(n - 2, -1, -1):
    size[-i - 1] = bisect.bisect_right(last_elem, numbers[i])  
    last_elem[size[-i - 1]] = numbers[i]
max_val = max(size)
print(max_val + 1)

elem = float('inf')
for i in range(n - 1, -1, -1):
    if numbers[-i - 1] <= elem and size[i] == max_val:
        print(n - i, end=' ')
        max_val -= 1
        elem = numbers[-i - 1]