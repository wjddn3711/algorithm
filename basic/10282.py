import heapq
from collections import deque

'''
최흉최악의 해커 yum3이 네트워크 시설의 한 컴퓨터를 해킹했다! 이제 서로에 의존하는 컴퓨터들은 점차 하나둘 전염되기 시작한다.
어떤 컴퓨터 a가 다른 컴퓨터 b에 의존한다면, b가 감염되면 그로부터 일정 시간 뒤 a도 감염되고 만다.
이때 b가 a를 의존하지 않는다면, a가 감염되더라도 b는 안전하다.

최흉최악의 해커 yum3이 해킹한 컴퓨터 번호와 각 의존성이 주어질 때,
해킹당한 컴퓨터까지 포함하여 총 몇 대의 컴퓨터가 감염되며 그에 걸리는 시간이 얼마인지 구하는 프로그램을 작성하시오.
'''

'''
기본적인 다익스트라 최단 경로 알고리즘 문제
도달할 수 있는 정점들의 개수와 최대 거리를 출력합니다
정점의 개수 N이 최대 10000 이고, 간선의 개수 D는 최대 100000입니다
우선순위 큐를 이용하여 시간 복잡도는 O(NlogD)로 해결할 수 있습니다
'''

def dijikstra(start):
    distance[start] = 0 # 자기 자신-> 자신 까지의 거리는 0으로 초기화
    data = [] # 우선순위 큐를 활용하기 위해 리스트를 하나 만들어줌
    heapq.heappush(data,(0,start)) # start 와 거리 정보를 힙에 담는다 (거리를 기준으로 우선순위가 설정 됨 )
    while data: # 이어져있는 모든 노드들을 이동하였을 때까지 반복
        dist, now = heapq.heappop(data) # 현재 노드(now)에 저장되어 있는 거리 = dist
        if dist > distance[now]: # 만약 현재 저장되어 있는 거리가 기존에 저장된 거리보다 크다면 최단 거리를 구할 필요가 없음
            continue
        for node in graph[now]: # 그래프에 저장된 node들을 순차적으로 담아줌
            cost = node[1] + dist # cost = now에서 다음 node까지의 거리
            if cost < distance[node[0]]: # 만약 이 cost 가 기존에 저장된 노드까지의 거리보다 크다면 고려 하지 않아도 됨
                heapq.heappush(data,(cost,node[0])) # 힙에 넣어준다
                distance[node[0]] = cost # 기존 거리정보를 최신 거리정보로 초기화



T = int(input())
for _ in range(T):
    n,d,c = map(int,input().split())
    # n = 컴퓨터의 개수, d = 의존성 개수, c = 해킹이 시작되는 컴퓨터
    INF = float('inf') # 임의의 무한대 값을 저장
    distance = [INF]*(n+1) # 처음에는 간선이 없다 생각하고 모두 무한대로 초기화
    graph = [[] for _ in range(n+1)] # 0번째를 재외하고 순서대로 n 까지 있다고 가정함
    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((a,s)) # a가 b에 의존하기 때문에 b에 a와 거리정보를 저장한다
    dijikstra(c) # 다익스트라 함수를 실행하면 distance 리스트 정보가 바뀐다
    maxVal = 0 # 임의로 최대 값을 0으로 설정해준다 ( 자기 자신과의 거리 최소 0 이기 떄문 )
    cnt = 0
    for dist in distance:
        if dist != INF: # 무한대인 경우는 감염되지 않았다는 것이기 때문에 제외한다
           cnt+=1 # 감염 횟수 +1
           if dist > maxVal:
               maxVal = dist # 현재 저장된 maxVal 보다 큰값일시 최대값으로 초기화
    print(cnt, maxVal)


