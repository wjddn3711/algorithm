import copy

n,m = map(int,input().split())
graph = []
cctv = []
for i in range(n):
    x = list(map(int,input().split()))
    for j in range(m):
        if x[j] != 0 and x[j] != 6: # 해당 장소에 cctv가 있다면
            cctv.append([i,j,x[j]]) # cctv 리스트에 좌표값과 해당 시시티비 종류를 더한다
    graph.append(x)

def checkSafeZone(ar): # 사각지대의 크기를 반환한다
    cnt = 0
    for i in range(n):
        for j in range(m):
            if ar[i][j]==0:
                cnt+=1
    return cnt

# 동북서남 방향벡터
dx = [0,-1,0,1]
dy = [1,0,-1,0]

# def fill(x,y,v,ar):
#     nx = dx[v]+x
#     ny = dy[v]+y
#     while 0<=nx<n and 0<=ny<m: # 맵의 범위를 벗어나지 않고
#         if ar[nx][ny]==0 or ar[nx][ny]=='#':
#             # 움직인 공간이 빈칸일경우에만 이동하여 맵에 채워준다
#             ar[nx][ny] = '#'
#             nx += dx[v]
#             ny += dy[v]
#         else: break
#     return ar
#
#
# def fillMap(x,y,k,v,g):
#     ar = []
#     if k==1:
#         ar = fill(x,y,v,g)
#     elif k==2: # 두가지 방향으로
#         tmp = fill(x,y,v,g)
#         v = (v+2)%4
#         ar = fill(x,y,v,tmp)
#     elif k==3: # 두가지 방향으로
#         tmp = fill(x,y,v,g)
#         v = (v+1)%4
#         ar = fill(x,y,v,tmp)
#     elif k==4: # 세가지 방향으로
#         tmp1 = fill(x,y,v,g)
#         v = (v+1)%4
#         tmp2 = fill(x,y,v,tmp1)
#         v = (v+1)%4
#         ar = fill(x,y,v,tmp2)
#     elif k==5: # 네가지 방향으로
#         tmp1 = fill(x,y,v,g)
#         v = (v+1)%4
#         tmp2 = fill(x,y,v,tmp1)
#         v = (v+1)%4
#         tmp3 = fill(x,y,v,tmp2)
#         v = (v+1)%4
#         ar = fill(x,y,v,tmp3)
#     return ar
#
#
# result = float('inf')
#
# def dfs(now,g):
#     global result
#     if now == len(cctv): # 모든 시시티비를 고려하였을때
#         result = min(checkSafeZone(g),result) #안전영역의 최소값을 초기화한다
#         return
#     x,y,k = cctv[now]
#     for i in range(4): # 각 시시티비를 네가지 방향으로 돌렸을 경우
#         after = fillMap(x,y,k,i,copy.deepcopy(g)) # 해당 방향벡터로 돌렸을때의 그래프를 탐색
#         [print(*x) for x in after]
#         print()
#         dfs(now+1,after) # 다음 depth 를 확인
#
#
# dfs(0,graph)
# print(result)

direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 2], [2, 1], [1, 3], [3, 0]],
             [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]


def watch(x, y, direction, tmp):
    for d in direction:
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx >= 0 and nx < m and ny >= 0 and ny < n and tmp[ny][nx] != 6:
                if tmp[ny][nx] == 0:
                    tmp[ny][nx] = '#'
            else:
                break


result = float('inf') # 최소값을 얻기위해 임의로 최대값을 담아준다
def dfs(now,g):
    global result
    if now == len(cctv): # 모든 시시티비를 탐색하였을 떄
        result = min(checkSafeZone(g),result)
        return
    x,y,k = cctv[now] # 현재 탐색중인 시시티비
    for d in direction[k]: # 해당 종류 시시티비에 해당하는 방향벡터를 꺼내온다
        tmp = copy.deepcopy(g)
        watch(x,y,d,tmp)
        dfs(now+1,tmp)

dfs(0,graph)
print(result)
