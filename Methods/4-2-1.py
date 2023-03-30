data = input()
f = {i:data.count(i) for i in set(data)}
tab = {i:'' for i in f}
if len(f) == 1:
    tab[data[0]] = '0'
while len(f) != 1:
    left, right = sorted(f, key = lambda x: f[x])[0], sorted(f, key = lambda x: f[x])[1]
    for i in tab:
        if i in left:
            tab[i] = '0'+ tab[i]
        elif i in right:
            tab[i] = '1'+ tab[i]
    f[left+right] = f[left] + f[right]
    del f[left]
    del f[right]
res = ''
for i in data:
    res += tab[i]
print(len(tab), len(res))
for i in sorted(tab):
    print(f'{i}: {tab[i]}')
print(res)