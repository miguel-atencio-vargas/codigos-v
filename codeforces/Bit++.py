n=int(input())
c=0
for i in range(n):
    s=input()
    try:
        s.index('+')
        c+=1
    except ValueError:
        c-=1
print(c)
