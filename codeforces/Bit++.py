n=int(input())
c: int = 0
for i in range(n):
    s=input()
    try:
        s.index('+')
        c+=1
    except ValueError:
        c-=1
print(c)