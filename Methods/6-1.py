def bin_s(arr, k):
    n, r = 0, len(arr) - 1
    while n <= r:
        m = n + (r - n)//2
        if arr[m] == k:
            return m + 1
        elif arr[m] > k:
            r = m - 1
        else:
            n = m + 1
    return -1
_n, *a = map(int, input().split())
_k, *b = map(int, input().split())
print(*(bin_s(a, i) for i in b))