n,t=map(int, input().split())
v = list(map(int, input().split()))
c=0
for i in v:
    t=t-i
    if t>=0: c+=1
print(c)