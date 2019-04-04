import math
t = int(input())
while t > 0:
    t = t-1
    s = input()
    i = s.index(' ')
    a = int(s[:i])
    b= int(s[i:])
    step = 0
    c = 0
    while a!=b:
        c = ''.join(list(reversed(str(a))))
        print(c)
        c = int(c)
        if c > a:
            a = c
            step = step +1
        else:
            a = str(a)
            b = str(b)
            suma = abs(int(a[len(a)-1]) - int(b[0]))
            a = a[:len(a)-1]+str(suma)
            step = step + suma
            a = int(a)
            b = int(b)
        print(step)