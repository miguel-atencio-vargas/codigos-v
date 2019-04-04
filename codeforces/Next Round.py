

n,k=map(int, input().split())
v = list(map(int, input().split()))
c=0
for i in range(n):
    val = v[i]
    if val >= v[k-1] and val>0: c+=1
print(c)

