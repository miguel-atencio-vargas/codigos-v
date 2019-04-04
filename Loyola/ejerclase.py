lista = []
while True:
    num  = raw_input('Ingrese un numero:  ')
    if num == '':
        break
    lista.insert(len(lista), int(num))


index = None
for x in range(len(lista)):
    mini = 100000004
    for i in range(x, len(lista)):
        if  lista[i] < mini:
            mini = lista[i]
            index = i
    aux = lista[x]

    lista[x]=mini
    lista[index]= aux
print(lista)
y = len(lista)-3
print(y)
print(lista[y])