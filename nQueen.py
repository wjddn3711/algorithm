n = int(input())
row = [0]*n

def check(x):
    for i in range(x):
        if row[i] == row[x]: # 같은 열에 있다면 false
            return False
        if x-i == abs(row[x]-row[i]): # 대각선에 위치한다면 x거리 == y거리
            return False
    return True

def dfs(x):
    global result
    if x==n: # n개의 x를 놓았다면
        result+=1
    else:
        for i in range(n):
            row[x] = i # row[x] 에 i 를 넣고 가능한지 확인
            if check(x): # 만약 가능하다면 다음 행을 계산
                dfs(x+1)