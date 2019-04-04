c = float(input())
l = int(input())
suma = 0
for i in range(l):
    s = input()
    index = s.index(' ')
    a = float(s[:index])
    b= float(s[index:])
    suma = suma+ (a*b)
total = suma*c
if total % 2 != 0:
    print(total)
else:
    total = str(total)
    print(total + '000000')