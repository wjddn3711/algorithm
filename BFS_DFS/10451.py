def bfs(data, start, cycle):
    for c in cycle: # 만약 이미 있는 cycle 내에 start 가 존재하는 상태라면 바로 cycle 을 반환
        if start in c:
            return cycle
    visited, needVisit = [],[]
    needVisit.append(start) # 시작 노드를 큐에 담는다

    while needVisit:
        node = needVisit.pop(0)
        if node not in visited: # 만약 방문하지 않은 노드라면
            visited.append(node) # 노드를 방문처리
            needVisit.append(data[node])
    cycle.append(visited)
    return cycle

#
# cases = int(input())
# cycles=[]
# for i in range(cases):
#     cycle = []
#     N = int(input())
#     data = list(map(int, input().split()))
#     graph = dict()
#     for i in range(N):
#         graph[i+1] = data[i] # 딕셔너리로 자료형을 이동
#     for d in data:
#         cycle = bfs(graph,graph[d],cycle)
#     cycles.append(len(cycle))
#
# for c in cycles:
#     print(c)


def newBfs(start):
    q = [start]
    while q:
        target = q.pop(0)
        if visited[target] == 0:
            visited[target] = 1 # 해당 타겟을 방문처리
            q.append(data[target])



cases = int(input())
for i in range(cases):
    cnt = 0
    N = int(input())
    visited = [1]+[0]*(N) #0번째를 제외하고 1번째부터 모두 비방문 처리
    data = [0]+list(map(int, input().split()))
    for i in range(1,len(data)):
        if visited[i] ==0:
            newBfs(data[i])
            cnt+=1
    print(cnt)