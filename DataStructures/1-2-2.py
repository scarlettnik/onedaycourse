import sys
sys.setrecursionlimit(25000)
n, parents = int(input()), [int(i) for i in input().split()]
a = [[] for i in range(n + 1)]
for i in range(n):
  a[parents[i]] += [i]

root=-1
def search_height(root):
    height = 0
    for child in a[root]:
        height = max(height,search_height(child)+1)
    return height
print(search_height(root))