from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
result = 0
maxVal = max(map(max,graph))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x,y,cnt,total):
    global result
    if result >= (4-cnt)*maxVal+total: # 나머지 블록들이 모두 최대값이라도 현재 최대값보다 작다면 반환
        return
    if cnt==4:
        result = max(result,total) # 서로 이어져 있는 테트로미노가 4개일때 최대값을 갱신
        return
    else:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= nx < n and 0<= ny < m and not visited[nx][ny]: # 아직 방문X, 범위를 벗어나지 않는다면
                if cnt==2: # 현재 두번째 블록을 수행중일때, 두번째를 기준으로 재귀를 통해 재 실행
                    visited[nx][ny] = True
                    dfs(x,y,cnt+1,total+graph[nx][ny]) # 현재 위치를 기준으로 이 부분을 제외하고 다른것들을 방문처리
                    visited[nx][ny] = False # 백트래킹
                # 두번째 블록이 아니라면
                visited[nx][ny] = True
                dfs(nx,ny,cnt+1,total+graph[nx][ny]) # nx,ny를 기준으로 dfs 실행
                visited[nx][ny] = False # 다시 방문 풀어주기

# 각 좌표에서 시작하여 테트로미노를 만들었을경우 최대인 경우를 탐색한다
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,1,graph[i][j])
        visited[i][j] = False # 다시 방문 X

print(result)

