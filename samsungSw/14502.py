from collections import deque
from copy import deepcopy

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

# 상하좌우 이동 벡터
dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0
def spread(): # 벽이 세워진 뒤 퍼졌을 때 안전영역을 구한다
    global result
    board = deepcopy(graph)
    q = deque()
    # 그래프에서 바이러스의 시작점을 모두 저장한다
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                q.append([i,j])

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]==0:
                q.append([nx,ny])
                board[nx][ny] = 2
    cnt=0
    for r in board:
        cnt+= r.count(0)

    result = max(result,cnt) # 이전에 저장된 결과값과 현재 탐색중인 그래프의 0의개수중 더 큰것을 찾는다


def makeWall(cnt):
    if cnt == 3:
        spread()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0

makeWall(0)
print(result)


