n = int(input())
p=0
for i in range(n):
    a,b,c = map(int, input().split())
    m=a+b+c
    if m >=2:
        p+=1
print(p)