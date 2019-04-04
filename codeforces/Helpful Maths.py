v = list(map(int, input().split('+')))
v.sort()
s=[];c=0
for i in range((len(v)*2)-1):
    if i %2==0:s.append(v[c]);c+=1
    else: s.append('+')
s = ''.join(str(x) for x in s)
print(s)

#forma mas optima:
# a=input()[::2]
# orde=sorted(a)
# print("+".join(orde))
