# dp[n] = dp[n-1] +dp[n-2]

'''
1. 빈 리스트 만들기(입력값에 따른)
2. 초기값을 설정
3. 점화식 기반으로 계산값 적용하기
4. 특정 입력값에 따른 계산값을 리스트에서 추출하기
'''

def tiling(n):
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    if n>=3:
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
    return dp[n]%10007

n = int(input())
print(tiling(n))