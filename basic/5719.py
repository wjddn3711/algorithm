import heapq
from collections import deque
import sys
input = sys.stdin.readline
'''
-다익스트라 최단 경로 알고리즘을 수행합니다
-다익스트라 최단 경로에 포함되는 모든 간선을 추적해야합니다
-초기 최단 경로에 포함된 간선을 제외한 뒤에 다시 최단 경로를 탐색합니다 

BFS를 이용하여 최단 경로에 포함되어 있는 모든 간선을 역으로 추적할 수 있습니다

'''
def dijikstra():
    distance[start] = 0 # 자기 자신의 거리 = 0
    data = []
    heapq.heappush(data,(0,start))
    while data:
        dist, now = heapq.heappop(data)
        if dist > distance[now]:
            continue
        for node in graph[now]:
            cost = node[1]+dist # cost = 현재노드에서 node까지의 거리
            if cost < distance[node[0]] and not dropped[now][node[0]]: # 만약 이미 저장된 거리 정보가 더 작다면 pass
                distance[node[0]] = cost
                heapq.heappush(data,(cost,node[0])) # 노드와 거리정보를 힙에 담아줌

def bfs():
    q = deque([end])
    while q:
        now = q.popleft()
        if now==start:
            continue
        for node,c in bfsGraph[now]:
            if distance[node]+c==distance[now]:
                dropped[node][now] = True
                q.append(node)

while True: # n,m 이 모두 0일때 종료
    INF = float('inf')
    n,m = map(int,input().split()) # 장소의 수, 도로의 수
    if n==0:
        break
    start,end = map(int,input().split()) # 시작점, 도착점
    graph = [[] for _ in range(n)] # 0~n-1 까지의 도로 정보
    bfsGraph = [[] for _ in range(n)]
    for _ in range(m):
        u,v,p = map(int,input().split())
        graph[u].append((v,p)) # u에서 v까지의 거리 P
        bfsGraph[v].append((u,p))
        # u 에서 v까지 가는 도로는 최대 한개이다 이를 이용하여 거의 거리를 계산하자
    dropped = [[False]*(n+1) for _ in range(n+1)]
    distance = [INF]*(n)
    dijikstra()
    bfs()
    distance = [INF]*(n)
    dijikstra()
    print((distance[end] if distance[end] != INF else -1))



