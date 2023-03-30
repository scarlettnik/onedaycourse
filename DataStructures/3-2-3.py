import re
a=input()
b=input()
c=[i for i in range(len(b)) if b.startswith(a, i)]
for i in range(len(c)):
    print(c[i],end=' ')