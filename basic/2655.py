'''
밑면이 정사각형인 직육면체 벽돌들을 사용하여 탑을 쌓고자 한다.
탑은 벽돌을 한 개씩 아래에서 위로 쌓으면서 만들어 간다.
아래의 조건을 만족하면서 가장 높은 탑을 쌓을 수 있는 프로그램을 작성하시오.

벽돌은 회전시킬 수 없다. 즉, 옆면을 밑면으로 사용할 수 없다.
밑면의 넓이가 같은 벽돌은 없으며, 또한 무게가 같은 벽돌도 없다.
벽돌들의 높이는 같을 수도 있다.
탑을 쌓을 때 밑면이 좁은 벽돌 위에 밑면이 넓은 벽돌은 놓을 수 없다.
무게가 무거운 벽돌을 무게가 가벼운 벽돌 위에 놓을 수 없다.

'''
# n = int(input()) # 벽돌의 수
# size, height, weight = [],[],[]
# for _ in range(n):
#     s,h,w = map(int, input().split())
#     size.append(s)
#     height.append(h)
#     weight.append(w)
#
# # dp = list([]*n for _ in range(n))# 최소 1개를 쌓을 수 있기 때문에 1로 초기화
# # dp[0].append(1)
# temp = []
# dp = [1] * n
# currMax = 1
# result = list([]*n for _ in range(n))
# for i in range(n):
#     result[i].append(i+1)
#     for j in range(i):
#         if size[i]<size[j] and weight[i]<weight[j]: #내림차순, 무게나 사이즈가 같은 벽돌은 없다
#             if dp[j]+1>dp[i]:
#                 dp[i] = dp[j]+1
#                 if len(result[i]+result[j])>len(temp):
#                     temp = result[i] + result[j]
#     result[i] = (temp if temp else [i+1])
#
# print(max(dp))
# [print(item) for item in result[dp.index(max(dp))]]


'''
문제 핵심 아이디어
- 가장 먼저 벽돌을 무게 기준으로 정렬합니다
- D[i] = 인덱스가 i 인 벽돌을 가장 아래에 두었을 때의 최대 높이
- 각 벽돌에 대해서 확인하며 D[i]를 갱신합니다
- 모든 0<=j<i 에 대하여, D[i] =max(D[i], D[j]+height[i]) if area[i] > area[j]
'''

n = int(input())
tower= [[0,0,0,0]] + [[i+1]+list(map(int, input().split())) for i in range(n)]
tower.sort(key = lambda x: x[3]) # 탑을 무게 중심으로 우선 정렬한다

dp = [0]*(n+1)
for i in range(1,n+1):
    for j in range(i):
        if tower[i][1] > tower[j][1]: # i번째 면적이 j 번째보다 크다면
            dp[i] = max(dp[i],dp[j]+tower[i][2]) # i위에 j 를 얹인다

# 높이를 가장 높게 가지는 dp 를 기준으로 트래킹하여 결과값 도출
result = []
maxVal = max(dp)
index = n
while index!=0:
    if maxVal == dp[index]: # 현재 index가 max 값일때
        result.append(tower[index][0]) # result 에 index값 추가
        maxVal -= tower[index][2] # 최대값에서 현재 인덱스의 높이를 빼줌
    index-=1
result.reverse()
print(len(result))
[print(item) for item in result]


