from collections import deque

T = int(input())
for _ in range(T):
    m,n,k = map(int,input().split())
    field = [[0]*m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        field[x][y] = 1


    def bfs(x,y):
        q = deque()
        q.append([x,y])
        dx = [-1,1,0,0] # 상하좌우
        dy = [0,0,-1,1] # 상하좌우
        field[x][y] = 0 # 방문 표시
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = dx[i]+x
                ny = dy[i]+y
                if 0<=nx<n and 0<=ny<m:
                    if field[nx][ny] == 1:# 이동한 좌표에 배추가 있고 지정된 필드안에 존재한다면
                        q.append([nx,ny])
                        field[nx][ny] = 0 # 재방문 하지 않도록 0으로 초기화
    cnt=0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                bfs(i,j)
                cnt+=1
    print(cnt)