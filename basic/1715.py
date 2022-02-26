import heapq
# 항상 꺼낼때 최소 묶음만 두개 꺼내어 더해나가면 최소 비교 횟수!
n = int(input())
q = []
for i in range(n):
    heapq.heappush(q,int(input()))

result = 0
while len(q)>1:
    card1 =heapq.heappop(q)
    card2 =heapq.heappop(q)
    heapq.heappush(q,card1+card2)
    result+=card1+card2

print(result)

