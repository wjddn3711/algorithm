

'''
- 일직선상의 각 책들을 원래의 위치에 놓아야합니다
- 0보다 큰 책들과 0보다 작은 책들을 나누어서 처리합니다
- 두개의 우선순위 큐를 이용하여 문제를 효과적으로 해결합니다
- 마지막 책을 놓을 때는 다시 0으로 돌아올 필요가 없으므로, 가장 먼 책을 마지막으로 놓습니다
'''
import heapq

'''
문제 풀이:
- 0을 기준으로 양수쪽, 음수쪽으로 나누어 담아준다
- 우선 각 리스트에서 하나씩 빼오고 최대로 들수 있는양 m-1 개씩 담는다 => reusult 에 더해준다
- 최대 힙을 통하여 가장 작은 원소부터 꺼내온다
'''

n, m = map(int,input().split())
bookList = list(map(int,input().split()))

negative = [] # 음수
positive = [] # 양수


for book in bookList:
    if book<0: # 만약 음수라면 그냥 담아준다
        heapq.heappush(negative,book)
    else: # 양수라면 최대힙이기때문에 음수값으로 담아준다
        heapq.heappush(positive,-book)

longest = max(-min(negative),max(positive))
# 최대로 이동하는 길이는 다시 돌아올일 없기 때문에 이후에 다 빼준다

result = 0 # 최대로 이동해야하는 거리
while negative:
    result += heapq.heappop(negative) # 가장 거리가 먼 값을 더해준다
    for _ in range(m-1): # 이미 하나를 빼냈기 때문에 m-1개를 더 꺼낼 수 있다
        if negative:
        # 가장 큰 값을 꺼냈기 때문에 돌아오는 비용밖에 들지 않는다 (이후에 result 에 2를 곱해준다 )
            heapq.heappop(negative)

while positive:
    result += heapq.heappop(positive) # 가장 거리가 먼 값을 더해준다
    for _ in range(m-1):
        if positive:
            heapq.heappop(positive)

print(-result*2-longest)



