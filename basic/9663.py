'''
핵심 아이디어
- N*N 크기의 체스보드 위에 퀸 N개를 서로 공격할 수 없게 배치시켜야 합니다
- 대표적인 백트래킹 문제입니다
- DFS를 이용하여 간단히 백트래킹 알고리즘을 구현할 수 있습니

- 각 행을 차례대로 확인하면서, 각열에 퀸을 놓는 경우를 고려합니다
    - 이때 위쪽 행을 모두 확인하며, 현재 위치에 놓을 수 있는지 확인합니다
'''


def check(x):
    for i in range(x): # x위의 행에 대하여 대각선, 같은 선상인지 확인
        if row[x]==row[i]:
            return False # 같은 열에 있다면 False
        if abs(row[x]-row[i])==x-i:
            # 열의 길이 == 행의 길이 -> 대각선에 위치
            return False
    return True


def dfs(x):
    global result
    if x == n: # 만약 마지막 열까지 퀸을 놓았다면
        result +=1
    else:
        for i in range(n):
            row[x] = i # x행에 i를 넣고 가능한지 판단
            if check(x): # (x,i)에 놓을 수 있다면 다음행으로
                dfs(x+1)


result = 0
n = int(input())
row = [0]*n # n개의 행에 대한 정보
dfs(0) # 0 번째 행부터 탐색
print(result)


