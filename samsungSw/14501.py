n = int(input())
plan = []

for i in range(n):
    t,p = map(int,input().split())
    plan.append([t,p])

# def solution(n):
#     dp = [[0] for _ in range(n+1)]
#     # 점화식 : d[i] = i 번째 날까지 최대 이익을
#     # i 번째 날은 i+1 번째 날 기준 수익과 i 번째 날 수익 + t[i]만큼 지난후의 수익중 큰값
#     for i in range(n-1,-1,-1):
#         if plan[i][0] + i > n: # n+1 일 이후에는 고려할 필요가 없기 때문에 무시
#             dp[i] = dp[i+1]
#         else:
#             dp[i] = max(plan[i][1] + dp[i+plan[i][0]],dp[i+1])
#     return dp
dp = [0 for _ in range(n+1)]
# 점화식 : d[i] = i 번째 날까지 최대 이익을
# i 번째 날은 i+1 번째 날 기준 수익과 i 번째 날 수익 + t[i]만큼 지난후의 수익중 큰값
for i in range(n-1,-1,-1):
    if plan[i][0] + i > n: # n+1 일 이후에는 고려할 필요가 없기 때문에 무시
        dp[i] = dp[i+1]
    else:
        dp[i] = max(plan[i][1] + dp[i+plan[i][0]],dp[i+1])
print(dp[0])

