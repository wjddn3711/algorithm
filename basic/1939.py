#
# # def solve(start,end):
# #     queue = graph[start]
# #     result = 0
# #     answer = 0
# #     while queue:
# #         node = queue.pop(0)
# #         if node[1] < result:
# #             continue
# #         result = node[1]
# #         if node[1] == end:
# #             answer = max(answer,result)
# #         for key, val in graph[node[0]]:
# #             if val <= result:
# #                 queue.append([key,val])
# #     return answer
# from collections import deque
#
# def bfs(med):
#     queue = deque([start])
#     visited = [False]*(len(graph)+1)
#     visited[start] = True
#     while queue:
#         node = queue.popleft()
#         for n, w in graph[node]:
#             if not visited[n] and w >= med:
#                 queue.append(n)
#                 visited[n] = True
#     print(visited)
#     return visited[end]
#
#
#
#
# n,m = map(int,input().split())
# graph = dict()
# s = float('inf')
# e = 0
# for _ in range(m):
#     a,b,c = map(int,input().split())
#     if a not in graph:
#         graph[a] = [[b,c]]
#     else:
#         graph[a].append([b,c])
#     if b not in graph:
#         graph[b] = [[a,c]]
#     else:
#         graph[b].append([a,c])
#     # 최소, 최대 가중치 확인
#     s = min(s,c)
#     e = max(e,c)
# start, end = map(int,input().split())
# result = start
# while s<=e:
#     mid = (s+e)//2
#     if bfs(mid): # 도달할 수 있다면
#         s = mid+1
#         result = mid
#     else:
#         e = mid-1
# print(result)

from collections import deque
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
def bfs(c):
    queue = deque([start_node])
    visited = [False] * (n + 1)
    visited[start_node] = True
    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visited[y] and weight >= c:
                visited[y] = True
                queue.append(y)
    return visited[end_node]
start = 1000000000
end = 1
for _ in range(m):
    x, y, weight = map(int, input().split())
    adj[x].append((y, weight))
    adj[y].append((x, weight))
    start = min(start, weight)
    end = max(end, weight)
start_node, end_node = map(int, input().split())
result = start
while(start <= end):
    mid = (start + end) // 2 # mid는 현재의 중량을 의미합니다.
    if bfs(mid): # 이동이 가능하므로, 중량을 증가시킵니다.
        result = mid
        start = mid + 1
    else: # 이동이 불가능하므로, 중량을 감소시킵니다.
        end = mid - 1
print(result)