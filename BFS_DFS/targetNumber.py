from collections import deque
answer = 0

numbers = [4, 1, 2, 1]
target = 4
n = len(numbers) # numbers의 길이를 저장
q = deque()
q.append([numbers[0],0]) # 시작점 양수일때, 음수일 경우를 모두 큐에 삽입
q.append([-numbers[0],0])
idx = 0
while q:
    num, idx = q.popleft()
    if idx<n-1: # 아직 완전히 탐색이 안되었다면 큐에 다음 인덱스값을 삽입
        idx +=1
        q.append([num+numbers[idx],idx])
        q.append([num-numbers[idx],idx])
    else:
        if num == target:
            answer+=1
print(answer)