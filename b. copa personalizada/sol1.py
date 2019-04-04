s = input()
longi = len(s)



filas = ((longi - 1) // 20) + 1
columnas = ((longi - 1) // filas) + 1


print(filas,' ', columnas)


asterisco = filas * columnas - longi


for i in range(asterisco):
    left = (columnas - 1) * i
    right = (columnas - 1) * (i + 1)
    print(s[left:right]+'*')


sobra = (columnas-1) * asterisco
for i in range(filas - asterisco):
    left = columnas * i + sobra 
    right= columnas*(i+1) + sobra
    print(s[left:right])
