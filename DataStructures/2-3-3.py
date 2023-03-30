import sys

lines = [[*map(int, line.split())] for line in sys.stdin]
n, m = lines[0]
r = [0] + lines[1]
parent = [i for i in range(n + 1)]
maxr = max(r)

for d, s in lines[2:]:
  while d != parent[d]: d = parent[d]
  while s != parent[s]: parent[s], s = d, parent[s]
  if d != s:
    r[d] += r[s]
    parent[s] = d
    if r[d] > maxr: maxr = r[d]
    
  print(maxr)