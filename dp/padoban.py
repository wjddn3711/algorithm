def pado(n):
    dp = [1 for _ in range(101)]
    for i in range(3, 101):
        dp[i] = dp[i-2]+dp[i-3]
    return dp[n-1]

T = int(input())
for i in range(T):
    print(pado(int(input())))