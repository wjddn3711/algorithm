from itertools import combinations
'''
핵심아이디어:
팀은 총 두개로 나뉜다
팀당 능력치를 더하기 위해서 다시 두명씩 짝지어 조합을 짠다
'''

n = int(input())
status = [list(map(int,input().split())) for _ in range(n)]

result = float('inf')
players = [i for i in range(n)]
for start in combinations(players,n//2): # n명의 플레이어들을 두개의 팀으로 나누는 조합
    link = list(set(players)-set(start)) # 링크팀은 전체 플레이어에서 스타트팀을 뺀 나머지 (차집합)
    linkStat, startStat = 0,0 # 각 링크팀 스텟과 스타트팀 스텟을 0으로 초기화

    for p1,p2 in combinations(start,2): # start팀에서 두명씩 짝지어 나오게 되는 조합
        startStat += status[p1][p2] + status[p2][p1] # 두명의 플레이어의 스텟을 더하여 준다
    for p1,p2 in combinations(link,2):
        linkStat += status[p1][p2] + status[p2][p1]

    result = min(result,abs(startStat-linkStat)) # 스타트팀과 링크팀 능력치의 차의 최소값을 구한다
    if result == 0: # 능력치의 차가 0이라면 더이상 구할 필요가 없기 때문에 break
        break

print(result)