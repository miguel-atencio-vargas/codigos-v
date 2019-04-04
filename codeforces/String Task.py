s = list(input())
vocales = ['A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y']
l = len(s)
i = 0
s1 = []
while l > 0:
    try:
        vocales.index(s[i])
    except ValueError:
        s1.append(s[i])
    i += 1
    l -= 1
s2 = []
j = 0
for i in range(len(s1) * 2):
    if i % 2 == 0:
        s2.append('.')
    else:
        s2.append(s1[j].lower())
        j += 1
print("".join(s2))
