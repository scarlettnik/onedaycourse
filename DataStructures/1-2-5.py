import sys

fm = lambda a, x: (x, max(x, a[-1][1]) if a else x)
n, *a, k = map(int, sys.stdin.read().split())
left, right = [], []

for i, e in enumerate(a):
    left.append(fm(left, e))
    if i + 2 > k:
        if not right:
            while left:
                right.append(fm(right, left.pop()[0]))
        print(fm(left, right.pop()[1])[1])