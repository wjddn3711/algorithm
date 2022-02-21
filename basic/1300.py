import heapq
n = int(input())
k = int(input())
b = []
for i in range(1,n+1):
    for j in range(1,n+1):
        heapq.heappush(b,i*j)
cnt =1
while cnt<k:
    heapq.heappop(b)
    cnt+=1

print(heapq.heappop(b))
