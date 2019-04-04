n=int(input())
while n>0:
    s = input()
    if len(s)>10:
        a = s[0]+str(len(s)-2)+s[len(s)-1]
        print(a)
    else:
        print(s)
    n-=1
    
