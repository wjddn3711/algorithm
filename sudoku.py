import copy

graph = [] # 스도쿠 맵 초기화
zeroList = [] # 0 들의 좌표를 저장
for i in range(9):
    m = list(map(int,input().split()))
    graph.append(m)
    for j in range(9):
        if m[j] == 0: # 0의 위치를 저장한다
            zeroList.append([i,j])

def check(x,y): # 해당 좌표에 존재할 수 있는지 판단
    nums = [i for i in range(1,10)]
    for i in range(9):
        if graph[i][y] in nums:
            nums.remove(graph[i][y])
        if graph[x][i] in nums:
            nums.remove(graph[x][i])
    # 3*3 영역을 확인하기 위해 열과 행의 시작위치를 몫을 통해 파악한다
    row = x//3
    col = y//3
    for i in range(row*3, (row+1)*3):
        for j in range(col*3, (col+1)*3):
            if graph[i][j] in nums: # 3*3 영역내에 존재하는 수를 빼낸다
                nums.remove(graph[i][j])

    return nums

flag = False
def solution(n):
    global flag
    if flag: return
    if n==len(zeroList): # 만약 모든 0 들이 숫자로 바뀌었다면 스도쿠 solved
        result = copy.deepcopy(graph)
        for r in result:
            print(*r)
        flag = True
        return result
    curr = zeroList[n] # 현재 처리중인 0
    x, y= curr[0],curr[1]
    numbers = check(x,y) # 현재 좌표로 체크 하였을때 가능한 숫자들의 리스트
    for number in numbers:
        graph[x][y] = number # 가능한 수로 채운뒤 다음 0을 확인
        solution(n+1)
        if flag: return
        graph[x][y] = 0 # 다시 0으로 초기화 하여 백트래킹

print(type(solution(0)))