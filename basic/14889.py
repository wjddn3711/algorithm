from itertools import combinations
n = int(input())
status = [list(map(int,input().split())) for _ in range(n)]
div = n//2
mems = [i for i in range(n)]
start = list(combinations(mems,div)) # 스타트 팀을 뽑는다 1~n까지중에서 n/2 개만큼

result = float('inf')
link = []
for team in start:
    link = list(set(mems)-set(team)) # 조합 A-B (차집합) 이 링크팀에 해당된다
    a,b = 0,0
    for x,y in combinations(team,2): # 무작위로 선정된 n/2의 멤버중 2명을 뽑아 능력치를 더한다
        a += status[x][y]+status[y][x]
    for x,y in combinations(link,2):
        b += status[x][y] + status[y][x] # 기존에 인덱스는 0부터 시작하기때문에 -1해준다
    result = min(result, abs(a-b)) # 스테이터스 스타트팀과 링크팀의 차를 구하여 최소가 되는 경우를 반환
print(result)



