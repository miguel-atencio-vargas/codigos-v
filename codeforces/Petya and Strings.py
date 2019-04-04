a=input().lower()
b=input().lower()
if a > b:print('1')
elif b > a: print('-1')
else: print('0')
#Codigo mas optimo e interesante
# i=input
# a=i().lower()
# b=i().lower()
# f1=a>b;f2=a<b
# print(f1-f2)

# Examples
# input
# aaaa
# aaaA
# output 
# 0
# input 
# abs
# Abz
# output 
# -1
# input 
# abcdefg
# AbCdEfF
# output 
# 1