n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)] # 테트로미노 맵
visited = [[False]*m for _ in range(n)]
# 위치 벡터 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

'''
ㅗ,ㅏ,ㅓ,ㅜ 의 경우를 제외하고는 한점에서 네번 벡터를 거치면 완성할 수 있다 
백트래킹을 이용하여 2개 까지 쌓은 경우 두번째 위치에서 다시 이동, 2개 가 아닐때는 그냥 이동하도록 하여
모든 경우를 탐색한다
'''
result = 0
maxVal = max(map(max,graph))
def dfs(x,y,cnt,s):
    global result
    if result >= (4-cnt)*maxVal+s: # 나머지가 모두 최대라도 result 보다 작다면 무시
        return
    if cnt==4:
        result = max(result,s)
        return
    else:
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<= nx < n and 0<= ny < m and not visited[nx][ny]:
                if cnt==2:
                    visited[nx][ny] = True
                    dfs(x,y,cnt+1,s+graph[nx][ny]) # x,y에서 다시 하나를 채운다
                    visited[nx][ny] = False # 백트래킹
                visited[nx][ny] = True
                dfs(nx,ny,cnt+1,s+graph[nx][ny]) # dfs 를 수행
                visited[nx][ny] = False # 백트래킹

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,1,graph[i][j])
        visited[i][j] = False

print(result)