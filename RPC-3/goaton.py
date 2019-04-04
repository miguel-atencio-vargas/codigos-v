i,j,x1,y1,x2,y2=map(int, input().split())

x1=abs(x1)
y2=abs(y2)
x2=abs(x2)
y2=abs(y2)
if j>y2:
    resp=j-y2
elif j<y1:
    resp = y1-j
elif i >x2:
    resp = i-x2
else:
    resp = x1-i

print(str(resp)+'.000')
