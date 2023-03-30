import sys
sys.setrecursionlimit(25000)

def in_order(tree, node, less, great):
    global result
    if result == 1:return
    if tree[node][0] >= less and tree[node][0] < great:
        if tree[node][1] != -1: in_order(tree, tree[node][1], less, tree[node][0])
        if tree[node][2] != -1: in_order(tree, tree[node][2], tree[node][0], great)
    else:result = 1
    
result, tree = 0, []
[(tree.append([int(i) for i in input().split()])) for _ in range(int(input()))]
in_order(tree, 0, -(2 ** 31), 2 ** 31) if tree and len(tree) > 1 else None
print('INCORRECT' if result else 'CORRECT')