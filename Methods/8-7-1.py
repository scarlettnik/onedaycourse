import sys
def f(steps: list, n: int) -> int:
    steps = [0] + steps
    pos = 2
    l, x = 0, steps[1]
    while pos < n + 1:
        l, x = x, max(l, x) + steps[pos]
        pos += 1
    return x
def main():
    n = int(sys.stdin.readline())
    steps = list(map(int, sys.stdin.readline().split()))
    print(f(steps, n))
if __name__ == '__main__':
    main()