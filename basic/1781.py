'''
각각의 데드라인에 대하여 매번 현재 시간을 계산하여 컵라면 수가 최대가 되도록 한다
- 데드라인을 초과하는 문제는 풀 수 없습니다
- 데이터의 개수 N은 최대 200000 입니다
- 정렬 및 우선순위 큐를 이용하여 O(NlogN)의 시간에 해결할 수 있습니다

'''
import heapq

n = int(input())
questions = []
result = []

# 문제 정보를 입력받은 이후에, 데드라인을 기준으로 정렬
for i in range(n):
    d,p = map(int,input().split())
    questions.append((d,p))
questions.sort()

for q in questions:
    a = q[0] #데드라인
    heapq.heappush(result, q[1]) #큐에 컵라면수를 담는다
    # 만약 데드라인을 넘는다면 최소원소를 제거
    # 해당 데드라인에서 최대값을 찾는 경우와 같음
    if a < len(result):
        heapq.heappop(result)
print(sum(result))