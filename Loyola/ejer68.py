a = int(input())
bill = [500, 200, 100, 50, 20 ,10, 5,2,1]
i = 0
tipo = ''
while a > 0:
    c = a//bill[i]
    if c > 0:
        a = a-(c*bill[i])
        if(bill[i]>=5): tipo = 'billete'
        else: tipo = 'moneda'
        print(c, tipo, 'de', bill[i], 'euros')
    i = i+1