vector = []
acc = 0
for x in range(0 , 5):
    vector.insert(x, input())
    acc = acc + vector[x]
print(acc/5)