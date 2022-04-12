n,l = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

def check(ar):
    visited = [False]*n # 경사로를 놓았는지 여부를 확인
    now = ar[0] # 시작점을 0번째 인덱스의 수로
    for i in range(1,n):
        if visited[i]: # 해당 칸에 경사로가 설치되었을 경우 pass
            continue
        if ar[i] == now: # 현재칸이 다음칸과 같은경우
            continue
        else: # 다음칸과 다를경우
            if abs(ar[i]-now) > 1: # 만약 둘의 높이차가 1을 넘을경우 성립 불가능
                return False
            else: # 둘의 높이차가 1인 경우
                if ar[i]+1 == now: # 현재 칸보다 다음칸이 작을경우
                    if i+l <= n: # 다음칸에 경사로를 놓을 수 있는 경우
                        tmp = ar[i]
                        for j in range(i,i+l):
                            if visited[j] or ar[j]!= tmp: # 해당 칸에 경사로가 있거나 다음칸과 값이 다를시 성립 불가능
                                return False
                            visited[j] = True # 아닐 경우 해당칸에 경사로를 놓는다
                        now = tmp # 경사로를 놓은 칸을 현재 칸으로 바꾼다
                    else: return False # 경사로를 넣을 수 없는 경우 False 반환
                elif ar[i]-1 == now: # 현재 칸보다 다음칸이 클경우
                    # ar[i-1] ~ ar[i-l-1] 만큼 가능한지 이전
                    if i-1-l>=0: # 이전 칸들에 경사로를 놓을 수 있는 경우
                        tmp = ar[i-1]
                        for j in range(i-1,i-1-l,-1):
                            if visited[j] or ar[j]!= tmp:
                                return False
                            visited[j] = True
                        now = ar[i] # 경사로를 놓았다면 다음칸을 현재 칸으로 초기화
                    else: return False
    return True
result = 0
for r in graph:
    print(check(r))
    if check(r):
        result +=1

for j in range(n):
    col = []
    for i in range(n):
        col.append(graph[i][j])
    if check(col):
        result+=1

print(result)