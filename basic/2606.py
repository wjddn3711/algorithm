from collections import deque

n = int(input()) #컴퓨터의 수
v = int(input()) #간선의 개수

graph = [[] for _ in range(n+1)] # 1번 부터기 때문에 0번째는 고려하지 않는다
for _ in range(v):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    # 컴퓨터 쌍을 저장해준다

visited = [False]*(n+1)
# 시작은 항상 1번 컴퓨터 부터
cnt =0
def bfs():
    global cnt
    q = deque([1])
    visited[1] = True
    while q:
        e = q.popleft()
        for node in graph[e]:
            if not visited[node]:
                q.append(node)
                visited[node]=True
                cnt+=1

bfs()
print(cnt)

