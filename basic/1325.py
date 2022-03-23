from collections import deque
'''
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다.
이 회사는 N개의 컴퓨터로 이루어져 있다.
김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.

이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데,
A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.

이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수
있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.


신뢰하는 관계 → 연결된 노드
'''

'''
모든 정점에 대하여 DFS 혹은 BFS 를 수행합니다
DFS 혹은 BFS를 수행할 때마다 방문하게 되는 노드의 개수를 계산합니다
가장 노드의 개수가 크게되는 시작 정점을 출력합니다
'''
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
result = [0]*(n+1)

for _ in range(m):
    x,y = map(int,input().split())
    graph[y].append(x)

def bfs(v, cnt):
    visited = [False]*(n+1)
    q = deque([v])
    visited[v] = True
    while q:
        node = q.popleft()
        for s in graph[node]:
            if not visited[s]:
                q.append(s)
                visited[s] = True
                cnt+=1
    return cnt

for i in range(1,n+1):
    if not graph[i]:
        result[i] = 0
    else:
        result[i] = bfs(i,0)

maxVal = max(result)
for i in range(1,len(result)):
    if result[i]==maxVal:
        print(i, end=' ')
