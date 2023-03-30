from bisect import bisect_left, bisect_right
n, m = map(int, input().split())
left, right = map(sorted, zip(*(map(int, input().split()) for _ in range(n))))
print(*(bisect_right(left, point) - bisect_left(right, point) for point in map(int, input().split())))