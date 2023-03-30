n, _ = map(int, input().split())
list = [input().split(': ') for _ in range(n)]
list = sorted((len(kod), kod, char) for char, kod in list)
s_k = input()

i, r = 0, ''
while i < len(s_k):
    for l, kod, char in list:        
        if kod == s_k[i: i + l]:
            r += char
            i += l
            break    
print(r)