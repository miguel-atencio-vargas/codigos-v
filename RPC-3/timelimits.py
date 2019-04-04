import math
n,s=map(int, input().split())
v = list(map(int, input().split()))
may=-2147483647
for i in v:
    if i>may:
        may=i
res = may*s
print(math.ceil(res/1000))