import heapq
operations = ["I 7","I 5","I -5","D -1"]
answer = []
minH = []
maxH = []
cnt = 0
for op in operations:
    a,n = op.split() # 공백을 기준으로 나누어 준다
    if a=='I': # 삽입명령시
        heapq.heappush(minH,int(n))
        heapq.heappush(maxH,-int(n))
    else:
        if int(n)<0: # 최소값을 삭제
            x = heapq.heappop(minH)
            maxH.remove(x)
        else: # 최대값을 삭제
            x = heapq.heappop(maxH)
            minH.remove(-x)

if minH: # 큐가 비어있다면
    answer = [0,0]
else:
    answer = [-heapq.heappop(maxH),heapq.heappop(minH)]
print(answer)