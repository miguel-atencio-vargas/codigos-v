  
while True:
    n= input()
    if n =='':
        break
    else:
        n=int(n)
        if n == 0: 
            print(0)
        elif n == 1 or n ==2: 
            print(1)
        else:
            j = n * [0] 
            j[0] = 1
            j[1] = 1
            for i in range(2, n):
                j[i]=j[i-1]+j[i-2]
            print(j[len(j)-1])