'''
총 k 번 회정 시킨 이후에 네 톱니바퀴의 점수의 합을 출력
각 톱니 바퀴별로 12시 방향의 극에 따라 점수를 합산
1 : N=0, S=1
2 : N=0, S=2
3 : N=0, S=4
4 : N=0, S=8
'''
import math
from copy import deepcopy

cogs = []
for _ in range(4):
    cog = list(map(int,input()))
    cogs.append(cog)

k = int(input())
commands = [list(map(int,input().split())) for _ in range(k)]

def turn(cog,command):
    p = deepcopy(cog)
    if command==1: # 반시계 방향으로 == 왼쪽으로
        for i in range(8):
            cog[i] = p[(i-1)%8]
    else: # 시계 방향으로 == 오른쪽으로
        for i in range(8):
            cog[i] = p[(i+1)%8]
    return cog


for c in commands:
    cog , command = c[0], c[1]
    change = [[0]*4 for _ in range(4)]
    for i in range(3):
        if cogs[i][2] != cogs[i+1][6]: # 맞닿은 톱니가 반대극이라면 회전하게 된다
            change[i][i+1] = 1
            change[i+1][i] = 1
    # 이전 톱니가 회전하지 않은경우 change가 1이더라도 회전되지 않는다
    cogs[cog-1] = turn(cogs[cog-1],command) # 해당 톱니를 우선 회전
    tc = command
    if cog==1: # 첫번째 톱니를 회전시키는 경우
        for i in range(1,4):
            if change[i][i-1]==0: break
            tc *= -1 # 해당 톱니가 바뀐다면 이전 톱니 회전의 반대 방향으로 바뀌게 된다
            cogs[i] = turn(cogs[i],tc)
    elif cog==2:
        if change[0][1]==1: # 첫번째 톱니가 바뀐다면
            cogs[0] = turn(cogs[0],-command)
        # 3, 4 번째 톱니를 확인
        for i in range(2,4):
            if change[i][i-1]==0: break
            tc *= -1 # 해당 톱니가 바뀐다면 이전 톱니 회전의 반대 방향으로 바뀌게 된다
            cogs[i] = turn(cogs[i],tc)
    elif cog==3:
        if change[3][2]==1: # 네번째 톱니가 회전된다면
            cogs[3] = turn(cogs[3],-command)
        for i in range(1,-1,-1): # 2~1 번째 톱니를 확인
            if change[i][i+1]==0: break
            tc *= -1
            cogs[i] = turn(cogs[i],tc)
    else: # 4번째 톱니를 회전시키는 경우
        for i in range(2,-1,-1): # 3번째 ~ 1번째 까지 체크
            if change[i][i+1]==0: break
            tc *= -1
            cogs[i] = turn(cogs[i],tc)

result = 0
for i in range(4):
    if cogs[i][0]==1: # S 극일때만 점수를 더해준다
        result+=math.pow(2,i) # 2의 i 승을 더해준다

print(int(result))


