from collections import deque

n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dice = [i+1 for i in range(6)]

# 동북서남 방향벡터
dx = [0,-1,0,1]
dy = [1,0,-1,0]

def moveDice(direction): # direction d를 매개변수로 받아 해당 방향으로 움직일때의 주사위 면을 바꾸어준다
    a,b,c,d,e,f = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]
    if direction==0: # 동쪽으로 움직일경우
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = d,b,a,f,e,c
    elif direction==1: # 북쪽으로 움직일경우
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = e,a,c,d,f,b
    elif direction==2: # 서쪽으로 움직일경우
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = c,b,f,a,e,d
    else: # 남쪽으로 움직일 경우
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = b,f,c,d,a,e

def bfs(x,y,val):
    cnt = 1
    visited = [[False]*m for _ in range(n)]
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4): # 네가지 방향으로 움직였을때에 같은것이 있다면 반환
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[nx][ny]==val: # 맵의 범위밖을 벗어나지 않으며
                # 이동한 칸에 해당값이 존재한다면 큐에 담는다
                q.append([nx,ny])
                visited[nx][ny] = True
                cnt+=1
    return cnt # 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수 C 를 반환한다

result = 0
x,y,p,d=0,0,0,0
while True:
# def rollDice(x,y,p,d):
    # global result
    if p==k: # 이동을 모두 완료 하였다면
        break
    # 해당 방향으로 이동후의 좌표
    nx = x+dx[d]
    ny = y+dy[d]
    # 이동한칸의 좌표가 맵을 벗어난다면
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        d = (d+2)%4 # 이동방향의 반대로 한칸 이동
        nx = x+dx[d]
        ny = y+dy[d]
    moveDice(d) # d 방향으로 주사위를 굴려 면을 맞춘다
    B = board[nx][ny]
    # 주사위가 도착한 칸에 대한 점수를 획득한다
    result += bfs(nx,ny,B)*B
    # 다음 이동 방향을 정한다
    A = dice[-1] # 주사위 아랫면에 있는 정수
    if A>B: # 90 도 시계방향으로 회전
        d = (d+3)%4
    elif A<B: # 90 도 반시계방향으로 회전
        d = (d+1)%4
    p+=1
    x = nx
    y = ny

print(result)