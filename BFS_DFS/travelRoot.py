import heapq
from collections import deque

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

answer = []
# '''
# - 항상 ICN 공항에서 출발
# - 두가지 경로가 존재한다면 알파벳 순서가 앞서는 순으로
# - 주어진 항공권을 모두 사용해야함
# '''
graph = dict()
for t in tickets:
    x,y = t
    if x not in graph:
        graph[x] = [y]
    else:
        heapq.heappush(graph[x],y)

result = []

def bfs(start):
    q = deque()
    q.append(start)
    result.append(start)
    while q:
        now = q.popleft()
        if len(result)==len(tickets)+1:
            return
        if graph[now]:
            x = heapq.heappop(graph[now])
            q.append(x)
            result.append(x)
bfs('ICN')
print(result)

