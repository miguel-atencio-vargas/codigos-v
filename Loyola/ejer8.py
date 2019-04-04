read = []
potencia = []
acc = 0
acc2 = 0
for x in range(5):
    read.insert(x, input())
    acc += read[x]
acc = acc / 5

for x in range(5):
    potencia.insert(x, (read[x] - acc) ** 2)
    acc2 += potencia[x]
print(acc2/5)