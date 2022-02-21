from heapq import *
n = int(input())
ar = []
for _ in range(n):
    heappush(ar,int(input()))
for _ in range(n):
    print(heappop(ar))