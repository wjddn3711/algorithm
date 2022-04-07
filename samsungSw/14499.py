n,m,x,y,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

# 동, 서, 북, 남 이동 벡터
dx = [0,0,-1,1]
dy = [1,-1,0,0]
dice = [0]*6 # 다이스의 면을 기준으로 값을 담아준다

def turn(dir):
    # 현재 각 번호 위치의 주사위 위치를 저장
    a,b,c,d,e,f = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]

    # 주사위를 이동 후 주사위 위치값 초기화
    if dir==1: # 동쪽으로 굴렸을때의 주사위
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = d,b,a,f,e,c
    elif dir==2: # 서쪽으로 굴렸을때
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = c,b,f,a,e,d
    elif dir==3: # 북쪽으로 굴렸을때
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = e,a,c,d,f,b
    else: # 남쪽으로 굴렸을때
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = b,f,c,d,a,e

commands = list(map(int,input().split()))


nx,ny = x,y
for c in commands:
    d = c-1
    nx+=dx[d]
    ny+=dy[d]
    # 이동 후 좌표
    if 0<= nx < n and 0<= ny < m:
        turn(c) # 주사위를 굴린다
        if board[nx][ny] == 0:
            board[nx][ny] = dice[-1] # 주사위의 바닥면의 수를 복사
        else:
            dice[-1] = board[nx][ny]
            board[nx][ny] = 0 # 칸에 있던 수를 바닥면에 복사, 바닥은 0으로
        print(dice[0]) # 주사위의 윗면을 출력
    else:
        nx-=dx[d]
        ny-=dy[d]
