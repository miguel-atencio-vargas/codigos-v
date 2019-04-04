

n = int(input())
v = list(map(int, input().split()))
n = 0
for i in v:
    if i < 0:
        n +=1
print(n)