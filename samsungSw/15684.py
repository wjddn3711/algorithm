'''
세로선의 개수 N, 가로선의 개수 M, 세로선마다 가로선을 놓을 수 있는 위치의 개수 H
즉 최대 가로선의 깊이는 H 임을 알 수 있다
이를 통하여 n*h 배열을 만들어 이미 주어진 가로선이 있을 경우 해당 위치는 True 로 바꾸어 처리한다
'''
n,m,h = map(int,input().split())
connect = [[False]*n for _ in range(h)]
for _ in range(m):
    a,b = map(int,input().split())
    connect[a-1][b-1] = True # 리스트는 0번째부터 시작하기에 -1 한 값으로 True 해준다


def check(): # i 번 세로선이 i 번으로 도착하는지 확인합니다
    for i in range(n):
        k = i
        for j in range(h): # 가로선 이동
            if connect[j][k]: # 가로선이 존재한다면
                k+=1 # 가로선 오른쪽으로 이동
            elif k > 0 and connect[j][k-1]: # 현재 세로선의 왼쪽에 가로선이 존재한다면
                k-=1 # 왼쪽으로 이동
        if k!=i: return False # 한번이라도 i 번 세로선이 i 번에 도착하지 않는다면 False
    return True

ans = float('inf')
def dfs(cnt,x,y):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans<=cnt: # 가로선을 3개 놓았는데 i번째가 i 에 도착하지 않는경우 혹은, 현재 저장된 최소값보다 클시 무효
        return

    # 가로선 탐색
    for i in range(x,h):
        if i==x:# 현재 행을 진행하고 있다면
            k=y
        else: # 현재행에 놓을 수 없는 경우 다음행 0부터 시작
            k=0
        for j in range(k,n-1):
            if not connect[i][j] and not connect[i][j+1]: # 현재 세로선에 연결된 가로선이 없으며 다음 세로선에도 현재 행에 가로선이 없다면
                if j>0 and connect[i][j-1]: # 왼쪽 세로선에도 가로선이 존재하면 안된다
                    continue
                connect[i][j] = True
                dfs(cnt+1, i, j+2) # i,j 에 가로선을 놓았을 때에 j+1 에는 놓을수 없으므로 j+2 부터 다시 가로선을 놓는 경우를 확인한다
                connect[i][j] = False # 유망하지 않다면 백트래킹

dfs(0,0,0)
print(ans if ans <= 3 else -1)