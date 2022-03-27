'''
R 과 C 의 범위가 작은 것으로 보아 모든 경우를 탐색해야 됨
인접한 칸에 같은 알파벳을 지난기록이 없는 경우

- 말은 상하좌우 네가지 방향으로 이동할 수 있습니다
- 지금까지 지나온 모든 칸에 적혀 있는 알파벳과 다른 알파벳이 적힌 칸으로 이동해야합니다
- 행의 길이 R 와 열의 길이 C가 20이하이므로, 백트래킹을 이용하여 모든 경우의 수를 고려합니다

'''

# 상하좌우 이동 좌표
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    global result
    q = set()
    q.add((x,y,board[x][y]))
    while q:
        x,y, step = q.pop()
        result = max(result, len(step))
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<r and 0<=ny<c and board[nx][ny] not in step:
                # 범위를 벗어나지 않고 이미 지나온 step 이 아닌경우
                q.add((nx,ny,board[nx][ny]+step))


r,c = map(int,input().split())
board = [input() for _ in range(r)]
result = 0
bfs(0,0)
print(result)
# 0,0 부터 시작하여 탐색을 시작
