a = input('ingrese un numero mayor que 20 y menor que 81: ')
u = 21
aux = a
sol = False
for x in range(1, 21):
    filas = 1
    rango = u-x
    print('rango', rango)
    while (a - rango) >= 0:
        
        filas = filas + 1
        a = a - rango
        if (a + 1) == rango or (a-1) == rango or a == rango:
            print('se ha encontrado la solucion optima')
            print('filas ', filas)
            print('col ', rango)
            sol = True
            break
    if(sol == True):
        break
    a = aux  


