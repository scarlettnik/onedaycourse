_ = int(input())
array = [[int(x)] for x in input().split()]
inv = 0
while len(array) != 1:
    new_a = []
    for i in range(0, len(array) - 1, 2):
        first, second = array[i], array[i + 1]
        new_s = []
        i, j = 0, 0
        n, m = len(first), len(second)
        while i < n and j < m:
            if first[i] <= second[j]:
                new_s.append(first[i])
                i += 1
            else:
                inv += len(first) - i
                new_s.append(second[j])
                j += 1
        new_s.extend(first[i:] if i < n else second[j:])
        new_a.append(new_s)
    if len(array) % 2:
        new_a.append(array[-1])
    array = new_a
print(inv)
