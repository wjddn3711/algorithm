from collections import deque

'''
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
'''
n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for item in graph:
    item.sort()

visit = [False]*(n+1)

def dfs(start):
    print(start, end=' ')
    visit[start] = True
    for e in graph[start]:
        if not visit[e]:
            dfs(e)


def bfs(start):
    visited = [0]*(n+1)
    queue = deque([start])
    while queue:
        item = queue.popleft() # 덱에 담긴 노드들을 하나씩 빼온다
        if visited[item] == 0:
            visited[item]= 1
            print(item, end=' ')
            for e in graph[item]:
                if visited[e]==0:
                    queue.append(e)

dfs(v)
print()
bfs(v)
