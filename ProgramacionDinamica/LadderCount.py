import math
def fibonacci(n):
    if n == 1: return [1]
    if n == 2: return [2]
    j = n * [0] 
    j[0] = 1
    j[1] = 2
    for i in range(2, n):
        j[i]=j[i-1]+j[i-2]
    return j

def solution(A, B):
    n = max(A)
    res = [0] * len(A)
    fib = fibonacci(n)
    for i in range(len(A)):
        res[i] = fib[A[i]-1] % int(math.pow(2, B[i]))
    print(res)
    return res


solution([50000,200,1000],[29,5,6])