
s = raw_input()

filas = 0
col = 0
resto = -1
longi = len(s)
aux = 19
cont = 1
for x in range(1, 21):
    if longi > 20:
        resto = longi - (x + aux)
        aux = aux - 1
        print(resto)


