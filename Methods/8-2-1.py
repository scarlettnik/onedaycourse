n = int(input())
list = [int(i) for i in input().split()]
nlist = [0] * n
for i in range(0, n):
    nlist[i] = 1
    for j in range(0, i):
        if (list[i] % list[j] == 0) and (nlist[j] + 1 > nlist[i]):
            nlist[i] = nlist[j] + 1
print(max(nlist))