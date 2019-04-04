

def cambio_base(decimal, base):
    conversion = ''
    while decimal // base != 0:
        conversion = str(decimal % base) + conversion
        decimal = decimal // base
    return str(decimal) + conversion

# numero = int(input('Introduce el número a cambiar de base: '))
# base = int(input('Introduce la base: '))
# print(cambio_base(numero, base))


while True:
    s = input()
    if s == '':
        break
    i = s.index(' ')
    base = int(s[:i])
    resto= s[i:]
    j=0
    for i in range(len(resto)-1):
        if resto[i] != '-' or resto[i]!='+':
            numeros[j] = resto[i]
            j = j+1
    print('base', base, 'resto', resto, 'numeros', numeros)