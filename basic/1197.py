
def findParent(x):
    if parent[x] == x:
        return x
    return findParent(parent[x])

def union(a,b):
    a = findParent(a)
    b = findParent(b)
    if a < b: # a가 b보다 작다면 b의 부모는 a 가 되도록 함
        parent[b] = a
    else:
        parent[a] = b

def check(a,b):
    a = findParent(a)
    b = findParent(b)
    if a==b: #둘이 같은 루트노드를 갖고 있다면 사이클이 생김
        return False
    return True

v,e = map(int,input().split())
parent = dict()
edges = []
for i in range(1,v+1):
    parent[i] = i # 자기자신을 루트로 초기화

for _ in range(e):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

edges.sort(key=lambda x:x[2])

result = 0
for a,b,c in edges:
    if check(a,b):
        union(a,b)
        result +=c

print(result)