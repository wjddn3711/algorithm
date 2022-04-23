
def findParent(x):
    if parent[x] == x: # 자기자신이 부모일때까지 계속
        return x
    return findParent(parent[x]) # 자기 자신이 부모가 아닐경우 자신의 부모의 부모를 찾는다

def isSameParent(x,y):
    x = findParent(x)
    y = findParent(y)
    if x==y: return True
    return False

def union(x,y):
    # 각각의 부모를 찾는다
    x = findParent(x)
    y = findParent(y)
    if x < y:# x의 부모가 y 의 부모보다 작다면 작은 쪽을 부모로
        parent[y] = x
    else:
        parent[x] = y

v,e = map(int,input().split())
parent = dict()

for i in range(1,v+1):
    parent[i] = i # 처음 각각 노드의 부모를 자기 자신으로 초기화 한다

result = 0
edges = []
for i in range(e):
    x, y, d = map(int,input().split())
    edges.append([x,y,d])

edges.sort(key=lambda x:x[2]) # 가중치를 기준으로 가중치가 작은것부터 이어주기 위해 정렬한다

for x,y,d in edges:
    if not isSameParent(x,y): # 같은 부모를 갖지 않는 다면 이어준다
        union(x,y)
        result+=d # 결과 가중치를 더해준다

print(result)
