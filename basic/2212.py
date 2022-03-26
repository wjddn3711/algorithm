import sys
'''
센서들은 직선 위의 한 기점인 원점으로부터 정수 거리의 위치에 놓여 있다
각 집중국의 수신 가능영역 거리의 합의 최소값을 구해야함
'''

'''
-최대 K개의 집중국을 설치해야 합니다
-집중국들의 수신 가능 영역의 길이의 합을 최소화 하는 것이 목표
-사실상 정렬만 수행하면 되므로 O(NlogN)으로 문제를 해결할 수 있습니

핵심 아이디어)
- 각 센서를 오름차순 정렬합니다
- 각 센서 사이의 거리를 계산합니다
- 가장 거리가 먼 순서대로 K-1개의 연결 고리를 제거합니다
'''
n = int(input()) # 센서의 개수
k = int(input()) # 집중국의 개수
sensors = list(map(int,input().split()))

if k>=n:
    print(0)
    sys.exit()

sensors.sort()# 센서의 위치를 오름차순으로 정렬
distances = [] # 각 센서간의 거리를 계산하여 내림차순 정렬
for i in range(1,n):
    distances.append(sensors[i]-sensors[i-1])
distances.sort(reverse=True)

# 가장 긴 거리부터 하나씩 제거
for i in range(k-1):
    distances[i] = 0
print(sum(distances))

