import sys
colors=[ 'azul', 'rojo', 'verde', 'amarillo']

def color_frecuente(v):
    c=[0,0,0,0]
    for i in range(len(v)):
        if v[i] == colors[0]:c[0]+=1
        elif v[i]==colors[1]:c[1]+=1
        elif v[i]==colors[2]:c[2]+=1
        elif v[i]==colors[3]: c[3]+=1
    maxi=-sys.maxsize
    for i in c:
        if  i>maxi:maxi=i
    for i in range(len(c)):
        if maxi==c[i]:
            return i,maxi
        


#i,m=color_frecuente(['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde', 'azul', 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo'])
i,m=color_frecuente(['rojo', 'rojo', 'azul', 'azul'])
print('El color:', colors[i],'aparece:', m)



