archivo = open("sample.in", 'r')
s=archivo.read().split()
for line in s:
    if line !=' ':
        print(line)
archivo.close() 