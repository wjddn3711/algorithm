'''
Day Of Mourning의 기타리스트 강토는 다가오는 공연에서 연주할 N개의 곡을 연주하고 있다.
지금까지 공연과는 다른 공연을 보여주기 위해서 이번 공연에서는 매번 곡이 시작하기 전에 볼륨을 바꾸고 연주하려고 한다.

먼저, 공연이 시작하기 전에 각각의 곡이 시작하기 전에 바꿀 수 있는 볼륨의 리스트를 만들었다.
이 리스트를 V라고 했을 때, V[i]는 i번째 곡을 연주하기 전에 바꿀 수 있는 볼륨을 의미한다.
항상 리스트에 적힌 차이로만 볼륨을 바꿀 수 있다.
즉, 현재 볼륨이 P이고 지금 i번째 곡을 연주하기 전이라면, i번 곡은 P+V[i]나 P-V[i] 로 연주해야 한다.
하지만, 0보다 작은 값으로 볼륨을 바꾸거나, M보다 큰 값으로 볼륨을 바꿀 수 없다.

곡의 개수 N과 시작 볼륨 S, 그리고 M이 주어졌을 때, 마지막 곡을 연주할 수 있는 볼륨 중 최댓값을 구하는 프로그램을 작성하시오.
모든 곡은 리스트에 적힌 순서대로 연주해야 한다.
'''

n, s, m = map(int, input().split())
v = list(map(int,input().split()))

def volume():
    dp = [0] * n
    for i in range(n):
        p = (s if i==0 else dp[i-1]) # 현재 볼륨 p
        if p+v[i] > m :
            if p-v[i] < 0 :
                return -1
            dp[i] = p-v[i]
        else:
            dp[i] = p+v[i]
    return max(dp)


# 2 번째 풀이
d = list([0]*(m+1) for _ in range(n+1))
d[0][s] = 1 # 초기값을 True 로 초기화
for i in range(1,n+1):
    for j in range(m+1):
        if d[i-1][j] == 1:
            if j+v[i-1] <= m :
                d[i][j+v[i-1]] = 1
            if j-v[i-1] >= 0 :
                d[i][j-v[i-1]] = 1

result = -1
for i in range(m,-1,-1):
    if d[n][i] == 1:
        result = i
        break
print(result)


'''
핵심 아이디어 : 모든 불륨에 대하여 연주 가능 여부를 계산하기
D[i][j+1] = i 번째 노래일 때, j 크기의 볼륨으로 연주 가능한지 여부
노래를 순서대로 확인하며, 매 번 모든 크기의 볼륨에 대하여 검사합니다
D[i][j-V[i]] = True if D[i-1][j] = True
D[i][j+V[i]] = True if D[i-1][j] = True
'''

