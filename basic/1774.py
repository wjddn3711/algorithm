

'''
- 2차원 좌표가 주어졌을때, 모든 좌표를 잇는 최소 신장 트리를 만들어야 합니다
- 따라서 2차원 좌표 상의 점을 잇는 통로들을 고려해야 합니다
- 정점의 개수 N이 최대 1000이므로, 가능한 통로의 개수는 약 N^2입니다
- 크루스칼 알고리즘은 간선의 개수가 E일때 O(ElogE)로 동작합니다
- 따라서 이 문제는 크루스칼 알고리즘으로 해결할 수 있습니다
'''
import math


def get_distance(p1,p2):
    x = p1[0] - p2[0] #x 좌표 차
    y = p1[1] - p2[1] #y 좌표 차
    return math.sqrt((x*x)+(y*y)) # 유클리드 거리 반환

def getParent(n):
    if parent[n] == n:
        return n
    else:
        return getParent(parent[n])

def getUnion(a,b):
    a = getParent(a)
    b = getParent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def isRoot(a,b):
    a = getParent(a)
    b = getParent(b)
    if a==b: # 같은 부모를 가진경우 이어주면 사이클이 생긴다
        return False
    else:
        return True


n,m = map(int,input().split())

# 기본적으로 사이클이 안생성되지만 각각의 노드가 서로 최소 거리로 연결되어있는 상태가 되도록 해야함

location = []
parent = {}
edges = []

for _ in range(n):
    x,y = map(int,input().split())
    location.append([x,y]) # x,y 좌표값을 저장

for i in range(1,n+1):
    parent[i] = i # 1부터 시작하여 n 까지... 초기 부모는 자신으로 초기화

# 각 좌표와 좌표간의 거리 정보를 edges 에 저장
length = len(location)
for i in range(1,length+1):
    for j in range(i+1,length+1):
        edges.append([i,j,get_distance(location[i-1],location[j-1])])

# 이미 연결된 경우 union
for _ in range(m):
    a,b = map(int,input().split())
    getUnion(a,b)

edges.sort(key=lambda x:x[2])

dist = 0
# edges 를 탐색하면서 사이클이 생기지 않는 경우에 서로 이어준다
for a,b,cost in edges:
    if isRoot(a,b):
        getUnion(a,b)
        dist+=cost
print('{0:0.2f}'.format(dist))