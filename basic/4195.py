# parent=[]
# def find(x):
#     if x==parent[x]: # x의 부모가 x 라면 즉, x가 루트노드라면
#         return x
#     else:
#         p = find(parent[x]) # 루트노드가 아니라면 재귀를 통하여 해당 부모를 찾는다
#         parent[x] = p
#         return parent[x]
#
# def union(x,y):
#     # 둘의 루트노드를 찾는다
#     x = find(x)
#     y = find(y)
#
#     if x!=y: # 둘의 부모노드가 다르다면 임의로 y의 부모를 x 로 두고 x의 네트워크 수를 늘려준다
#         parent[y] = x
#         number[x] += number[y]
#
#
# t = int(input())
# for _ in range(t):
#     parent = dict()
#     number = dict()
#
#     f = int(input())
#     for _ in range(f):
#         x, y = input().split()
#
#         if x not in parent:
#             parent[x] = x
#             number[x] = 1
#         if y not in parent:
#             parent[y] = y
#             number[y] = 1
#
#         union(x,y)
#         print(number[find(x)])


def find(x):
    if x == parent[x]: # x의 부모가 x라면 (루트노드라면)
        return x
    else:
        p = find(parent[x]) # x의 부모를 재귀적으로 계속 호출하여 루트 노드를 찾는다
        parent[x] = p
        return parent[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if x!=y: # x와 y의 루트노드가 다르다면
        parent[y] = x # 임의로 y의 부모를 x로 만든다
        number[x] +=number[y] #y의 네트워크수를 x 로 옮겨준다

t = int(input())
for _ in range(t):
    n = int(input())
    parent = dict()
    number = dict()
    for _ in range(n):
        x,y = input().split()
        if x not in parent: # 만약 초기화 된적이 없다면
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x,y)
        print(number[find(x)])

