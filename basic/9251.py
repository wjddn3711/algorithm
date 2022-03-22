'''
DP 문제 )
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때,
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
'''

str_1 = input()
str_2 = input()


dp = list([0]*(len(str_2)+1) for _ in range(len(str_1)+1))
for i in range(len(str_1)+1):
    for j in range(len(str_2)+1):
        if i==0 or j==0: # 공집합인 경우 0 으로 초기화
            dp[i][j] = 0
            continue
        if str_1[i-1] == str_2[j-1]: # 값이 같을 경우 대각선의 값에 +1
            dp[i][j] = dp[i-1][j-1]+1
        else: # 값이 다를경우 왼쪽과 위쪽중 더 큰값
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp[len(str_1)][len(str_2)])
