n,c = map(int, input().split())
h = [int(input()) for _ in range(n)]
h.sort()

minL = 1
maxL = h[-1]-h[0]
result = 0
while minL <= maxL:
    cnt = 1
    gap = (maxL+minL)//2 # 공유기 사이의 거리는 최소 거리+최대 거리로 초기화 해준다
    start = h[0] # 첫번째 집을 기준으로 탐색을 시작한다
    for i in range(1,len(h)):
        if h[i] - start >= gap: # 다음집과 기준점의 사이가 갭보다 크거나 같다면 성립 가능!
            cnt+=1
            start=h[i] #기준점 또한 바꿔준다
    if cnt< c: #c개의 공유기를 설치할 수 없다면
        maxL = gap-1
    else:
        minL = gap+1
        result = gap
print(result)
