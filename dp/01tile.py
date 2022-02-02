def tile(n):
    dp = [0 for _ in range(1000001)] # 0번째 인덱스를 제외하고
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = (dp[i-1]+dp[i-2])%15746
    return dp[n]

print(tile(int(input())))