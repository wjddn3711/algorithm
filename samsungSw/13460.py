'''
제한사항)
상하좌우로 움직일 수 있습니다
- 빨간구슬과 파란구슬은 같은칸에 존재할 수 없습니다
- 빨간구슬과 파란구슬이 동시에 빠져도 실패입니다
- 빨간 구슬만 구멍에 빠지도록 해야합니다
- . : 빈칸, # : 장애물, O : 구멍위치, R : 빨간구슬, B : 파란구슬
'''
from collections import deque

n,m = map(int,input().split())
rx,ry,bx,by = 0,0,0,0
board = [] # 보드 맵
for i in range(n):
    x = input()
    for j in range(m):
        if x[j] == 'R': # 빨간공의 위치를 저장한다
            rx,ry = i, j
        if x[j] == 'B': # 파란공의 위치를 저장한다
            bx,by = i, j
    board.append(x)

# 상하좌우 벡터
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def move(x,y,ndx,ndy):
    cnt = 0 # 움직인 횟수
    while board[x][y] != 'O' and board[x+ndx][y+ndy] != '#':
        # 구멍위치에 위치하거나 이동한 이후 좌표가 장애물이 아닐경우 계속 끝까지 이동
        x += ndx
        y += ndy
        cnt+=1
    return [x,y,cnt] # 움직인 횟수를 반환


def bfs():
    q = deque()
    q.append([rx,ry,bx,by,1]) # 공들의 위치와 이동횟수 1을 큐에 담는다
    visited = [] # 이미 방문한 좌표들을 저장한다
    visited.append([rx,ry,bx,by]) # 시작 점을 방문처리한다
    while q:
        nrx,nry,nbx,nby,cnt = q.popleft()
        if cnt > 10:
            break # 10번이상 움직일 경우 break
        for i in range(4):
            mrx, mry, mRcnt = move(nrx,nry,dx[i],dy[i]) # 이동후 빨간공
            mbx, mby, mBcnt = move(nbx,nby,dx[i],dy[i]) # 이동후 파란공
            if board[mbx][mby] != 'O':
                if board[mrx][mry] == 'O': # 이동 이후 탈출지점에 도착했다면
                    print(cnt)
                    return
                if mrx==mbx and mry==mby: # 만약 두공의 위치가 같다면 cnt 를 기준으로 많이 움직인 공을 한칸뒤로 빼준다
                    if mRcnt > mBcnt:
                        mrx -= dx[i]
                        mry -= dy[i]
                    else:
                        mbx -= dx[i]
                        mby -= dy[i]

                if [mrx,mry,mbx,mby] not in visited: # 이동후의 좌표가 방문한적이 없다면 이동해준다
                    visited.append([mrx,mry,mbx,mby])
                    q.append([mrx,mry,mbx,mby,cnt+1])
    print(-1)
bfs()
