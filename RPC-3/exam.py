c = int(input())
yo = input()
amigo = input()
same = 0
for i in range(len(amigo)):
    if amigo[i]==yo[i]:
        same+=1
dife = len(yo)-same

sobra = 0
if same>c:
    resp =c
    sobra = same-c
else:
    resp = same



if same ==0:
    resp = dife-c
else:
    resp+=dife
print(resp)