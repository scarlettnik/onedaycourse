n,m=map(int,input().split())
f,i = [0,1,1],3
while  f[0:2]!=f[i-2:]:
    f += [(f[i-1]+f[i-2])%m]    
    i+=1    
f = f[:len(f)-2]
print(f[n%len(f)])