import heapq as hq
n = int(input())
ar = []
result = []
for _ in range(n):
    x = int(input())
    if x==0:
        if ar:
            result.append(hq.heappop(ar))
        else:
            result.append(0)
    else:
        hq.heappush(ar,x)

for r in result:
    print(r)