import heapq as h
n,m = map(int, input().split())
degree = [0]*(n+1) # 가중치 리스트
ques = [[] for i in range(n+1)] # 각 문제당 선행되어야 할 문제가 있다면 해당 문제에 append
for _ in range(m):
    x,y = map(int, input().split())
    ques[x].append(y)
    degree[y] +=1

heap=[]
result = []
for i in range(1,n+1):
    if degree[i] == 0: # 가중치가 0인것을 힙에 담아준다
        h.heappush(heap,i)

while heap:
    data = h.heappop(heap)
    result.append(data)
    for q in ques[data]:
        degree[q] -=1 # 간선을 없앤다, 가중치 -1
        if degree[q] == 0: # 해당 노드의 간선이 없다면 힙에 추가해준다
            h.heappush(heap,q)

print(*result)