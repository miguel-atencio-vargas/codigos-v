import sys
s = input()
dp= [[0]for i in range(len(s))] 
for i in range(len(s)):
    dp[i] = int(s[i])

for x in range(len(s)):
    mini = 10000
    for i in range(x, len(dp)):
        if  dp[i] < mini:
            mini = dp[i]
            index = i
    aux = dp[x]
    dp[x]=mini
    dp[index]= aux


dp2= [[0] for i in range(10)] 
dp3= [0 for i in range(10)] 
for i in range(10):
    suma =0
    for y in range(len(dp)):
        if dp[y] == i:
            suma = suma +1
    dp2[i] = suma




for x in range(len(dp2)):
    mini = 1000000
    for i in range(x, len(dp2)):
        if dp2[i] < mini:
            mini = dp2[i]
            index = i
    aux = dp2[x]          
    dp2[x]= mini
    dp2[index] = aux

    




print(dp2)
print(dp3)



