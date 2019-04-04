def binarySearch(arreglo, num):
    left, right = 0, len(arreglo) -1
    while(left <= right):
        index = (left + right) // 2
        medio = arreglo[index]
        if medio == num:
            return index
        if num < medio:
            right = index - 1
        else:
            left = index + 1
    return -1



lista = []
while True:
    num  = raw_input('Ingrese un numero:  ')
    if num == '':
        break
    lista.insert(len(lista), int(num))
index = None
for x in range(len(lista)):
    mini = 10000
    for i in range(x, len(lista)):
        if  lista[i] < mini:
            mini = lista[i]
            index = i
    aux = lista[x]
    lista[x]=mini
    lista[index]= aux
print(lista)


busqueda = input('Ingrese un numero para buscar en la lista ordenada: ')
print('Se encuentra en la posicion: {}'.format(binarySearch(lista, busqueda)))
mini = 1000
for x in range(len(lista)):
    if lista[x] < mini:
        mini = lista[x]

maxi = -1000        
for x in range(len(lista)):
    if lista[x] > mini:
        maxi = lista[x]        
print('El menor es: {}'.format(mini))
print('El mayor es: {}'.format(maxi))

