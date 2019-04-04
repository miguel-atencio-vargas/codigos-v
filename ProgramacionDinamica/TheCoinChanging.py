import sys
def dynamic_coin_changing(C, k):
    n = len(C)
    # create two-dimensional array with all zeros
    dp = [[0] * (k + 1) for i in range(n + 1)]
    dp[0] = [0] + [sys.maxsize] * k

    
    for i in range(1, n + 1):
        for j in range(C[i - 1]):
             dp[i][j] = dp[i - 1][j]
        for j in range(C[i - 1], k + 1):
            dp[i][j] = min(dp[i][j - C[i - 1]] + 1, dp[i - 1][j])
    for i in range(n):
        print(dp[i])
    return dp[n]
print('respuesta: ', dynamic_coin_changing([1,3,4], 6))
