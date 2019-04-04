col = 6
fil = 3
#Llena la matriz con valores de 0
dp = [[0] * col for i in range(fil)] 
#Llena solo una fila[0] de la matriz con el valor de 8
dp[1] =  [8] * (col)


#imprime la matriz
for i in range(fil):
    print(dp[i])
