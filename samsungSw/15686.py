from itertools import combinations
'''
0: 빈칸, 1: 집, 2: 치킨집
'''
graph = []
house = []
chicken = []
n,m = map(int,input().split())
for i in range(n):
    x = list(map(int,input().split()))
    for j in range(n):
        if x[j] == 1:
            house.append([i,j])
        elif x[j] == 2:
            chicken.append([i,j])
    graph.append(x)

def getDist(r1,c1,r2,c2):
    return abs(r1-r2)+abs(c1-c2)

ans = float('inf')
# x 개의 치킨집중 m 개를 뽑는 조합을 생각하여 처리한다
for c in combinations(chicken,m):
    cDist = [float('inf')]*len(house)
    for x,y in c: # 각 치킨집의 좌표를 얻어온다
        for i in range(len(house)):
            cDist[i] = min(cDist[i], getDist(x,y,house[i][0],house[i][1]))
    ans = min(ans, sum(cDist))

print(ans)