'''
직각 삼각형의 각변 a,b,c 중 b 가 주어졌을 때 b 가 될 수 있는 최소값을 찾아내기
'''
from itertools import combinations
from copy import deepcopy
rocks = [2, 14, 11, 21, 17]
distance = 25
n = 2
answer = 0
'''
이분 탐색을 위해서 mid 값을 설정하여야 한다
이때에 반환되는 거리의 최소값중 가장 큰 값을 mid 값으로 지정한다
'''
for combi in combinations(rocks,n):
    A = sorted(list(set(rocks)- set(combi)))
    minD = A[0]
    for i in range(1,len(A)):
        if i == len(A)-1:
            minD = min(distance-A[i],minD)
        else:
            minD = min(A[i]-A[i-1], minD)
    answer = max(minD, answer)
print(answer)


