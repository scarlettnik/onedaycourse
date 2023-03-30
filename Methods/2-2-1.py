f1 = f2 = 1
n = input("")
n = int(n) - 2
while n > 0:
    f1, f2 = f2, f1 + f2
    n -= 1
print(f2)