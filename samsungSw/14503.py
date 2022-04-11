'''
로봇 청소기는 다음과 같이 작동한다.

1. 현재 위치를 청소한다.
2. 현재 위치에서 다음을 반복하면서 인접한 칸을 탐색한다.
    현재 위치의 바로 왼쪽에 아직 청소하지 않은 빈 공간이 존재한다면, 왼쪽 방향으로 회전한 다음 한 칸을 전진하고 1번으로 돌아간다.
    그렇지 않을 경우, 왼쪽 방향으로 회전한다. 이때, 왼쪽은 현재 바라보는 방향을 기준으로 한다.

    1번으로 돌아가거나 후진하지 않고 2a번 단계가 연속으로 네 번 실행되었을 경우, 바로 뒤쪽이 벽이라면 작동을 멈춘다.
    그렇지 않다면 한 칸 후진한다.
'''
n, m = map(int,input().split())
x,y,d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
result = 1 # 현재 위치를 청소하기 때문에 1부터 시작
def dfs(x,y,cnt):
    global result,d
    if cnt==4:
        back = (d+2)%4
        nx = x+dx[back]
        ny = y+dy[back]
        if graph[nx][ny] == 2:
            dfs(nx,ny,0)

        else:
            print(result)
            exit(0)
    # 현재 위치의 왼쪽에 청소하지 않은 공간이 존재한다면 ? 그리고 벽이 아니라면?
    d = (d+3)%4
    nx = x + dx[d]
    ny = y + dy[d]
    if 0<nx<n-1 and 0<ny<m-1 and graph[nx][ny]==0: #각 모서리는 벽이기 때문에 pass
        graph[nx][ny] = 2
        result +=1
        dfs(nx,ny,0) #왼쪽 방향으로 회전한 다음 한 칸을 전진하고 1번으로 돌아간다
    else: #그렇지 않을 경우, 왼쪽 방향으로 회전한다.
        dfs(x,y,cnt+1)

graph[x][y] = 2
dfs(x,y,0)
