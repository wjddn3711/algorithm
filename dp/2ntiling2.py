def tiling(n):
    dp = [0 for _ in range(1001)]
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = (dp[i-2]*2 + dp[i-1])%10007
    return dp[n]
n = int(input())
print(tiling(n))