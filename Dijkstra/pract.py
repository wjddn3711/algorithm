'''
1단계 : 초기화
    첫 정점을 기준으로 배열을 선언하여 첫 정점에서 각 정점까지의 거리를 저장
        초기에는 첫 정점의 거리는 0, 나머지는 무한대로 저장
        우선순위 큐에 (첫정점, 거리 0 ) 만 먼저 넣음

2단계 : 우선순위 큐에서 추출한 노드, 첫 노드와의 거리를 기반으로 인접한 노드와의 거리를 계산
    처음에는 첫 정점만 저장되어 있으므로, 첫 정점이 꺼내짐
    첫 정점에서 인접한 노드들 각가에 대해, 첫 정점에서 각 노드로 가는 거리가 더짧을 경우, 배열에 해당 노드의 거리를 업데이트
    배열에 해당 노드의 거리가 업데이트 된 경우, 우선순위 큐에 넣는다
        결과적으로 BFS 와 유사하게, 첫 정점에 인접한 노드들을 순차적으로 방문
        만약 배열에 기록된 현재까지 발견된 가장 짧은 거리보다, 더 긴거리를 가진 경우에는 업데이트 X

'''
'''
# heapq 라이브러리 활용을 통해 우선순위 큐 사용하기
import heapq
queue = []
heapq.heappush(queue,[2,'A'])
heapq.heappush(queue,[5,'B'])
heapq.heappush(queue,[1,'C'])
heapq.heappush(queue,[7,'D'])
print(queue)

for i in range(len(queue)):
    print((heapq.heappop(queue)))
'''
import heapq
graph = {
    'A':{'B':8,'C':1,'D':2},
    'B':{},
    'C':{'B':5,'D':2},
    'D':{'E':3,'F':5},
    'E':{'F':1},
    'F':{'A':5}
}

# def dijk(graph, start, end):
#     dist = {node:float('inf') for node in graph} # 거리를 모두 무한대로 초기화
#     dist[start] = 0 # 자신에서 자신까지 거리는 0
#     queue = []
#
#     heapq.heappush(queue,[dist[start],start])
#     while queue:
#         currentDist, currentNode = heapq.heappop(queue)
#         if dist[currentNode] < currentDist: # 만약 현재 비교중인 노드의 거리가 기존 저장된 노드의 거리보다 크다면 고려하지 않고 스킵
#             continue # 다음 노드로 스킵
#
#         for adjacent, weight in graph[currentNode].items():
#             distance = currentDist+ weight # 거리는 현재까지 노드의 거리 + 가중치
#             if distance < dist[adjacent]: # 만약 해당 거리가 현재 저장된 거리보다 짧다면 초기화 후 힙에 저장
#                 dist[adjacent] = distance
#                 heapq.heappush(queue,[distance,adjacent])
#     return dist
#
# print(dijk(graph,'A'))


def dijiks(start, end, graph):
    dist = {node:[float('inf'),start] for node in graph} # 그래프에 있는 노드의 개수만큼 [무한대, 이전 시작점] 을 마킹해준다
    queue = []
    heapq.heappush(queue,[0,start]) # 우선순위 큐를 활용하여 시작점을 0으로 초기화후 힙에 넣어준다
    dist[start] = [0,start]
    while queue: # 더이상 업데이트 할게 없을때까지 반복한다
        currentDist, currentNode = heapq.heappop(queue) # 큐에서 현재 가중치와 노드를 꺼내온다
        if dist[currentNode][0] < currentDist: # 만약 기존 저장된 노드의 거리가 현재 비교하는 대상의 거리보다 작다면 무시하고 다음으로 진행
            continue
        for target, weight in graph[currentNode].items():
            # 현재 노드와 연결된 타겟과 타겟가중치를 통하여 비교를 진행
            distance = currentDist+weight # 비교될 거리는 기존 저장된 거리 + 타겟가중치
            if distance < dist[target][0]:
                # 기존 타겟 노드의 거리보다 비교될 거리가 더 작다면 해당 노드를 힙에 저장
                dist[target] = [distance,currentNode]
                heapq.heappush(queue,[distance,target])
    mark = end
    while dist[end][1] != start:
        end = dist[end][1]
        mark+= ' -> '+end
    mark += ' -> ' +start
    return mark, dist



# 방향 그래프
mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

mark, dist = dijiks('A','F',mygraph)
print(mark)
