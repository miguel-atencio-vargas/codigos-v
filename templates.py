
#para crear un vector de n tamaño
n=5
v= [0 for i in range(n)] 
#print(v)

#para leer en una sola linea
# n,m = map(int ,input().split())
# # para leer una linea de tamaño n y meterlo en un vector
# v = list(map(int, input().split()))


#para pasar de una lista a cadena 
a=['hola' , 'estoy' , 'haciendo' , 'un' , 'programa']
cadena = " ".join(a)


#para obtener el ascii de un char
a = 'A'
print(ord(a))
#para obtener la minuscula de un char
print(a.lower())

# para crear e imprimir una matriz
m = [[0]*10 for i in range(10)] 
for i in m:
    a=''
    for j in i:
        a+=str(j)+' '
    print (a)

#para dividir palabras
a = 'hello world'

s = a.index(' ')



s = 'abcd'
s = s[:len(s)-1]
print(s)




#ternario
#resultado = valor_si if condicion else valor_no



#para unir o pasar de lista a string y convertirlos a str
###si todo es str solo se pone la cadena como argumento
s = ''.join(str(x) for x in s)
#para leer de salto en salto en salto donde 3 indica de cuanto en cuanto salta
a=input()[::3]