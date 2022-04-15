k, n = map(int,input().split())
cables = [int(input()) for _ in range(k)]

result = 0
start,end = 1,max(cables)
while start <= end:
    mid = (start+end)//2 # N 개를 만들수 있는 랜선의 최대 길이

    cut = 0
    for c in cables:
        cut+= c//mid

    if cut >= n: # 자른 횟수가 n 보다 같거나 많을 경우 더 길게 잘라야 하므로 start를 옮겨준다
        start = mid+1
        result = mid
    else: # 자른 횟수가 n 보다 작다면 더 짧게 잘라야 하므로 end를 옮겨준다
        end = mid-1

print(result)