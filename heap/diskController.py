import heapq
jobs = [[0, 3], [1, 9], [2, 6]]
disk = []
for r,t in jobs:
    heapq.heappush(disk,[t,r])

temp = []
result = 0
currT = 0
while disk:
    while temp:
        heapq.heappush(disk,temp.pop())
    curr = heapq.heappop(disk)
    if curr[1] <= currT: # 현재 시간보다 요청이 들어온 시간이 더 적다면 작업 수행
        currT += curr[0]
        result += currT-curr[1]
    else:
        temp.append(curr)

print(result)