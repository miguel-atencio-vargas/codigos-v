import math
a = float(input())
b = float(input())
c = float(input())
s =  a+b+c
print('perimetro:', s)
s = s / 2
print('area:',math.sqrt(s*(s-a) * (s-b)* (s-c)))
