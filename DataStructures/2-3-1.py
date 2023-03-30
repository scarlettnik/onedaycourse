n = int(input())
c = [int(i) for i in input().split()]
d = dict(zip(c, range(n)))
out = sorted(c)
dout = dict(zip(range(n), out))
res = []
for j in range(n - 1):
    b = d[dout[j]]
    if c[j] != out[j]:
        d[c[b]] = j
        d[c[j]]  = b
        c[j], c[b] = c[b], c[j]
        res.append([j, b])
print(len(res))
[print(i[0], i[1]) for i in res]
