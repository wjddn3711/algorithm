import heapq
n = int(input())
nums = [int(input()) for _ in range(n)]
heapq.heapify(nums)
for i in range(len(nums)):
    print(heapq.heappop(nums))
    # 힙 과 스택의 차이