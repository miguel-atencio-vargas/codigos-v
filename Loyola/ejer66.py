a = int(input())
b = int(input())

c = a**2
if b == c:
    print('El segundo es el cuadrado exacto del primero')
elif b<c:
    print('El segundo es menor que el cuadrado del primero')
else:
    print('El segundo es mayor que el cuadrado del primero')
