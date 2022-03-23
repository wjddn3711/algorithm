n = int(input())
A = list(map(int, input().split()))
dp = [1]*n
'''
점화식 : dp[i] = A[i]를 마지막 원소로 갖는 최대 길이의 수열
각각 최소 1개씩 갖고 있다 
'''

for i in range(1,n):
    for j in range(i):
        if A[j]<A[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))
