def walk(i, f):
    return () if i == -1 else \
           (i for s in f(walk(tree[i][1], f), walk(tree[i][2], f), tree[i][0]) for i in s)

tree = [list(map(int, input().split())) for _ in range(int(input()))]
print(*walk(0, lambda left, right, val: (left, [val], right)))
print(*walk(0, lambda left, right, val: ([val], left, right)))
print(*walk(0, lambda left, right, val: (left, right, [val])))