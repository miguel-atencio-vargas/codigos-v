import sys
m = [[' ']*1000 for i in range(1000)] 
indL=499
indR=499

indU=499
indB=499
i = 499
j = 499
def move(s, h='*'):
    global i, j ,indL, indR, indU, indB
    if s =='right':
        j +=1
        if m[i][j]=='S': j+=1
        if j>indR: indR=j
        m[i][j] = h
    elif s =='left':
        j -=1
        if m[i][j]=='S': j-=1
        if j<indL: indL=j
        m[i][j]=h
    elif s == 'up':
        i -=1
        if m[i][j]=='S': i-=1
        if i < indU:indU=i
        m[i][j]=h
    else:
        i +=1
        if m[i][j]=='S': i+=1
        if i > indB: indB=i
        m[i][j]=h
m[i][j]='S'
aux=''

# while True:
#     s = input()
#     if s=='':
#         break
#     else:
#         aux = s
#         move(s)

# for line in sys.stdin:
#     aux=line
#     move(line)
archivo = open("sample.in", 'r')
s=archivo.read().split()
for line in s:
    if line !=' ':
        move(line)
archivo.close() 

m[i][j]='E'

k=0
for i in m:
    i=i[indL-1:indR+2]
    i[0]='#'
    i[len(i)-1]='#'
    m[k]=i
    k+=1
m=m[indU-1: indB+2]
m[0]=['#' for i in range(len(m[0]))]
m[len(m)-1]=['#' for i in range(len(m[0]))]

for i in m:
    a=''
    for j in i:
        a+=j
    print (a)