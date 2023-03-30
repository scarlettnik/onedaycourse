import sys
sys.setrecursionlimit(25000)

n = int(input())
tree = []

for _ in range(n):
    tree.append(tuple(map(int, input().split())))
in_order = []
def get_in_order(v):
    v[1] != -1 and get_in_order(tree[v[1]])
    in_order.append(int(v[0]))
    v[2] != -1 and get_in_order(tree[v[2]])
if n !=0:
    get_in_order(tree[0])
if in_order==[] or all(in_order[i] <= in_order[i+1] for i in range(len(in_order)-1)):
    print('CORRECT')
else:
    print('INCORRECT')