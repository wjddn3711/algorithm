from collections import deque

n= 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

answer = 0


def bfs(x,y):
    q = deque()
    q.append(x)
    computers[x][y] = 0 # 방문처리
    while q:
        now = q.popleft()
        for i in range(len(computers[now])):
            if computers[now][i] == 1:
                q.append(i) # 큐에 i 번째 컴퓨터를 삽입
                computers[now][i]=0 # 방문처리




for i in range(n):
    for j in range(n):
        if computers[i][j]==1:
            answer+=1
            bfs(i,j)

print(answer)