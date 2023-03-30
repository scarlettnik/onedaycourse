list = []
for _ in range(int(input())):
    c = input().split()
    if c[0] == 'push':
        list.append(int(c[1]) if not list or int(c[1]) > list[-1] else list[-1])
    elif c[0] == 'pop' and list: list.pop()        
    elif c[0] == 'max' and list: print(list[-1])