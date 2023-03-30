m = n = int(input())
k, i = [], 1
while m > 0:
    k += [i]
    m -= i
    i += 1 
sum = sum(k) - n
if sum > 0:
    k.pop(sum - 1)
print(len(k))
print(*k)