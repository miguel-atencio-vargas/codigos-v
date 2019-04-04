s = input()

c=0
for i in range(len(s)-1):
    if s[i]==s[i+1] and c<6:
        c+=1
    elif c<6: 
        c=0

if c>=6:print('YES')
else:print('NO')
#El codigo mas optimo:
# print(["NO","YES"][7*"1"in s or 7*"0"in s])
#tambien:
#print('YES' if ('0'*7 in m or '1'*7 in m) else 'NO')

# Examples
# inputCopy
# 001001
# outputCopy
# NO
# inputCopy
# 1000000001
# outputCopy
# YES